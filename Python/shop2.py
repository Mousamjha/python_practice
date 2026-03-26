import json
import os
import random
import time
from datetime import datetime

# ============================ CONSTANTS / CONFIG ============================
SHOP_NAME = "Shri Siddhant's Shop"
VERSION = "3.0 Ultra"

GLOBAL_SALE_OFF = 0.50            # flat 50% off on paid items
SESSION_FLASH_SALE_CHANCE = 5     # 1 in N chance for extra sale
SESSION_FLASH_SALE_EXTRA = 0.05   # +5%
GST_RATE = 0.18
LOW_STOCK_THRESHOLD = 3
EMI_MIN_TOTAL = 300
EMI_MONTHLY_INTEREST = 0.01
LOYALTY_EARN_RATE = 0.05
LOYALTY_MAX_REDEEM_RATE = 0.50
WALLET_CASHBACK_RATE = 0.10

SAVE_FILE = "shopverse_save.json"

# Reputation bands
REPUTATION_BANDS = [
    ( -999, "Outlaw"),
    (  -50, "Shady"),
    (   -5, "Risky"),
    (    5, "Neutral"),
    (   50, "Trusted"),
    (  999, "Honored"),
]

# Cities and travel costs
CITIES = {
    "Market Street": 0,
    "Downtown": 20,
    "Slums": 5,
    "Luxury Plaza": 50,
    "Black Alley": 15,
}

WEATHERS = ["Clear", "Rain", "Heat", "Cold", "Storm"]
TIMES_OF_DAY = ["Morning", "Afternoon", "Night"]

# Shopkeeper behaviours and templates
BEHAVIOURS = {
    "polite": {
        "greet": [
            "Welcome. Glad to see you.",
            "Good to see you. Please take your time.",
        ],
        "deal": ["I can give a fair deal."]
    },
    "greedy": {
        "greet": ["We have good things. Prices are firm."],
        "deal": ["No free stuff. Business is business."]
    },
    "scammer": {
        "greet": ["Only today, special price. Trust me."],
        "deal": ["Bill will be adjusted later. Do not worry."]
    },
    "rude": {
        "greet": ["Buy fast or leave."],
        "deal": ["No questions. Pay now."]
    },
    "nervous": {
        "greet": ["Hello. I am a bit busy. Please be quick."],
        "deal": ["I am not sure. Let me check."]
    },
    "mafia_backed": {
        "greet": ["Prices are final. We have protection."],
        "deal": ["Do not test me. Pay as shown."]
    },
    "friendly": {
        "greet": ["Friend, welcome back.", "You look well today."],
        "deal": ["I can give you a small cut."]
    },
}

# Items and stock
PRICES = {
    1: 10,   # scissors
    2: 5,    # envelopes
    3: 30,   # iPhone 14 cover black
    4: 30,   # iPhone 14 cover
    5: 20,   # AirPods cover
    6: 50,   # iPhone 15 cover T&J
    7: 10,   # bottle opener
    8: 30,   # stapler pins
    9: 0,    # stapler (free with pins)
    10: 500  # Raymond wallet
}

MENU = {
    1: "Red & Black scissors",
    2: "Pack of Envelopes",
    3: "iPhone 14 cover 'black'",
    4: "iPhone 14 cover",
    5: "Apple AirPods cover",
    6: "iPhone 15 cover Tom and Jerry",
    7: "Bottle opener",
    8: "Stapler Pins",
    9: "Stapler (Free with Pins)",
    10:"Raymond Limited Edition Wallet"
}

DEFAULT_STOCK = {
    1: 1,
    2: 25,
    3: 1,
    4: 1,
    5: 1,
    6: 1,
    7: 1,
    8: 7,
    9: 1,
    10:1,
}

# Coupon system
COUPON_PRICE_POOL = [10, 20, 30]
COUPON_EFFECTS = [
    "flat_off", "percent_off", "free_stapler",
    "cashback_after_payment", "double_points", "nothing",
    # new hidden effects
    "waive_gst", "extra_warranty", "police_immunity",
]

# ============================ UTILITIES ============================

def now_str():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def band_for_rep(rep):
    for threshold, name in REPUTATION_BANDS:
        if rep <= threshold:
            return name
    return "Neutral"


def ask_int(prompt):
    s = input(prompt).strip()
    return int(s) if s.isdigit() else None


def pause(s=1):
    time.sleep(s)

# ============================ STATE CLASSES ============================
class DialogueRecorder:
    def __init__(self):
        self.lines = []
    def say(self, who, text):
        line = (now_str(), who, text)
        self.lines.append(line)
        print(f"{who}: {text}")
    def sys(self, text):
        self.say("System", text)
    def evaluate(self):
        total = len(self.lines)
        pos = sum(1 for _,_,t in self.lines if any(k in t.lower() for k in ["thank","welcome","good"]))
        neg = sum(1 for _,_,t in self.lines if any(k in t.lower() for k in ["police","jail","angry","problem"]))
        print("\n=== DIALOGUE REPORT ===")
        print(f"Total lines: {total}")
        print(f"Positive lines: {pos}")
        print(f"Conflict lines: {neg}")
        print("=======================\n")


class Coupon:
    def __init__(self, cid, price, effect):
        self.id = cid
        self.price = price
        self.effect = effect
        self.redeemed = False
    def label(self):
        return f"Coupon {self.id}"


class Player:
    def __init__(self, name="Customer"):
        self.name = name
        self.reputation = 0
        self.wallet = 0
        self.loyalty_points = 0
        self.city = "Market Street"
        self.health = 100
        self.hunger = 0
        self.inventory = {}
        self.coupons = []
        self.coupon_cost_total = 0
        self.flags = {
            "police_immunity": False,
        }
    def add_item(self, item_id, qty):
        self.inventory[item_id] = self.inventory.get(item_id, 0) + qty
    def remove_item(self, item_id, qty):
        if self.inventory.get(item_id,0) >= qty:
            self.inventory[item_id] -= qty
            if self.inventory[item_id] == 0:
                del self.inventory[item_id]
            return True
        return False


class Shop:
    def __init__(self):
        self.stock = DEFAULT_STOCK.copy()
        self.behaviour = random.choice(list(BEHAVIOURS.keys()))
        self.session_extra_sale = SESSION_FLASH_SALE_EXTRA if random.randint(1, SESSION_FLASH_SALE_CHANCE) == 1 else 0.0
        self.free_stapler_given = False
        self.time_of_day = random.choice(TIMES_OF_DAY)
        self.weather = random.choice(WEATHERS)
        self.dialogue = DialogueRecorder()

    # ---------- Present info ----------
    def banner(self):
        print(f"==================== {SHOP_NAME} ({VERSION}) ====================")
        print(f"City: {player.city} | Weather: {self.weather} | Time: {self.time_of_day}")
        band = band_for_rep(player.reputation)
        print(f"Reputation: {player.reputation} ({band}) | Wallet: Rs.{player.wallet} | LP: {player.loyalty_points}")
        sale_pct = int((GLOBAL_SALE_OFF + self.session_extra_sale) * 100)
        print(f"Sale: {sale_pct}% off today on paid items. GST: {int(GST_RATE*100)}% (if applied)")
        print("Type /help for commands.")

    def display_menu(self):
        print("\nAvailable Items:")
        for k in sorted(MENU.keys()):
            if self.stock[k] > 0:
                if k == 9:
                    print(f"{k}: {MENU[k]} ({self.stock[k]} left)")
                else:
                    price = PRICES[k]
                    print(f"{k}: {MENU[k]} - Rs.{price} ({self.stock[k]} left)")
                    if self.stock[k] < LOW_STOCK_THRESHOLD:
                        print(f"  Note: Low stock on {MENU[k]}")

    def all_sold_out(self):
        return all(q == 0 for q in self.stock.values())

    # ---------- Behaviour speech ----------
    def greet(self):
        t = random.choice(BEHAVIOURS[self.behaviour]["greet"]) if self.behaviour in BEHAVIOURS else "Hello."
        self.dialogue.say("Shopkeeper", t)

    # ---------- Search ----------
    def search(self, keyword):
        key = keyword.lower()
        results = []
        for num, name in MENU.items():
            if key in name.lower() and self.stock[num] > 0:
                results.append((num, name, PRICES[num], self.stock[num]))
        if results:
            print("Search results:")
            for num, name, price, stk in results:
                print(f"  {num}: {name} - Rs.{price} ({stk} left)")
        else:
            print("No items found.")

    # ---------- Cart ops ----------
    def add_to_cart(self, cart, item_id, qty):
        # stock check
        if item_id not in MENU:
            print("No such item.")
            return False
        if item_id == 9:
            print("Stapler is free only with Stapler Pins.")
            return False
        if qty <= 0 or qty > self.stock[item_id]:
            print("That item is not in stock.")
            return False
        # free stapler with pins once
        if item_id == 8 and (not self.free_stapler_given) and self.stock[9] > 0:
            cart[9] = cart.get(9, 0) + 1
            self.stock[9] -= 1
            self.free_stapler_given = True
            self.dialogue.say("Shopkeeper", "You will get one stapler free with your pins.")
        self.stock[item_id] -= qty
        cart[item_id] = cart.get(item_id, 0) + qty
        print(f"Added {qty} x {MENU[item_id]} to your cart.")
        return True

    def remove_from_cart(self, cart, item_id, qty):
        if cart.get(item_id, 0) < qty or qty <= 0:
            print("Cannot remove that amount.")
            return False
        cart[item_id] -= qty
        if cart[item_id] == 0:
            del cart[item_id]
        self.stock[item_id] += qty
        print("Cart updated.")
        return True

    # ---------- Coupons ----------
    def buy_coupon(self):
        cid = f"C-{random.randint(1000,9999)}"
        price = random.choice(COUPON_PRICE_POOL)
        effect = random.choice(COUPON_EFFECTS)
        c = Coupon(cid, price, effect)
        player.coupons.append(c)
        player.coupon_cost_total += price
        self.dialogue.say("Shopkeeper", f"Here is a sealed coupon: {c.label()}. Price is Rs.{price}.")
        print("The effect is secret until you redeem it at billing.")

    def buy_all_coupons(self):
        n = random.randint(2,5)
        for _ in range(n):
            self.buy_coupon()
        print(f"You bought {n} sealed coupons.")

    # ---------- Billing ----------
    def compute_totals(self, cart, loyalty_redeem_points, apply_gst, used_coupon):
        sale_total = GLOBAL_SALE_OFF + self.session_extra_sale
        line_items = []
        base_subtotal = 0
        # cart lines
        for iid, qty in cart.items():
            unit = PRICES[iid]
            total = unit * qty
            line_items.append((iid, MENU[iid], unit, qty, total))
            base_subtotal += total
        # coupon cost as line item
        if player.coupon_cost_total > 0:
            line_items.append(("COUPONS", "Coupons purchased", player.coupon_cost_total, 1, player.coupon_cost_total))
            base_subtotal += player.coupon_cost_total
        sale_discount = int(round(base_subtotal * sale_total))
        def sale_price(item_id):
            return int(round(PRICES[item_id] * (1 - sale_total)))
        # offers
        offer_discount = 0
        env_qty = cart.get(2, 0)
        if env_qty >= 10:
            offer_discount += int(round(sale_price(2) * env_qty * 0.10))
        covers_qty = cart.get(3, 0) + cart.get(4, 0)
        if covers_qty >= 3:
            free_units = covers_qty // 3
            offer_discount += min(sale_price(3), sale_price(4)) * free_units

        # pre-secret
        pre_secret = max(0, base_subtotal - sale_discount - offer_discount)
        secret_note = ""
        secret_discount = 0
        cashback_flag = False
        double_points = False
        waive_gst = False
        extra_warranty = False
        police_immunity = False

        if used_coupon and not used_coupon.redeemed:
            eff = used_coupon.effect
            if eff == "flat_off":
                secret_discount = 50
                secret_note = "Secret coupon: flat off"
            elif eff == "percent_off":
                secret_discount = int(round(pre_secret * 0.10))
                secret_note = "Secret coupon: percent off"
            elif eff == "free_stapler":
                if self.stock[9] > 0:
                    secret_note = "Secret coupon: free stapler"
                    cart[9] = cart.get(9, 0) + 1
                    self.stock[9] -= 1
                else:
                    secret_note = "Secret coupon: stapler out of stock"
            elif eff == "cashback_after_payment":
                secret_note = "Secret coupon: cashback after payment"
                cashback_flag = True
            elif eff == "double_points":
                secret_note = "Secret coupon: double points"
                double_points = True
            elif eff == "waive_gst":
                secret_note = "Secret coupon: GST waived"
                waive_gst = True
            elif eff == "extra_warranty":
                secret_note = "Secret coupon: warranty extended"
                extra_warranty = True
            elif eff == "police_immunity":
                secret_note = "Secret coupon: police immunity"
                police_immunity = True
            else:
                secret_note = "Secret coupon: no effect"
            used_coupon.redeemed = True

        pre_redeem = max(0, pre_secret - secret_discount)
        max_redeem = int(round(pre_redeem * LOYALTY_MAX_REDEEM_RATE))
        redeem_used = min(loyalty_redeem_points, max_redeem)
        pre_tax_total = max(0, pre_redeem - redeem_used)
        gst_amount = 0 if waive_gst else int(round(pre_tax_total * GST_RATE)) if apply_gst else 0
        grand_total = pre_tax_total + gst_amount

        points = int(round(pre_tax_total * LOYALTY_EARN_RATE))
        if double_points:
            points *= 2

        return {
            "line_items": line_items,
            "base_subtotal": base_subtotal,
            "sale_discount": sale_discount,
            "offer_discount": offer_discount,
            "secret_note": secret_note,
            "secret_discount": secret_discount,
            "redeem_used": redeem_used,
            "pre_tax_total": pre_tax_total,
            "gst_amount": gst_amount,
            "grand_total": grand_total,
            "points_earned": points,
            "cashback_flag": cashback_flag,
            "extra_warranty": extra_warranty,
            "police_immunity": police_immunity,
        }

    # ---------- Payment ----------
    def payment(self, amount):
        print("Select payment method: 1 Cash | 2 UPI | 3 Card | 4 Net | 5 Wallet")
        pm = input("Enter option: ").strip()
        if pm == "1":
            while True:
                paid_s = input(f"Enter cash received (due Rs.{amount}): ").strip()
                if not paid_s.isdigit():
                    print("Enter a number.")
                    continue
                paid = int(paid_s)
                if paid < amount:
                    print("Less than total. Collect full amount.")
                    continue
                if paid > amount:
                    print(f"Change to return: Rs.{paid - amount}")
                self.dialogue.say("Shopkeeper", "Cash received.")
                return True, "Cash"
        elif pm in ("2","3","4"):
            self.dialogue.say("Shopkeeper", "Processing payment.")
            pause(1)
            self.dialogue.say("Shopkeeper", "Payment successful.")
            return True, {"2":"UPI","3":"Card","4":"Net"}[pm]
        elif pm == "5":
            if player.wallet >= amount:
                player.wallet -= amount
                self.dialogue.say("Shopkeeper", "Paid from wallet.")
                return True, "Wallet"
            else:
                need = amount - player.wallet
                print(f"Wallet has Rs.{player.wallet}. Need Rs.{need} more.")
                top = input("Top up wallet now? (yes/no): ").strip().lower()
                if top == "yes":
                    add_s = input("Enter top up amount: ").strip()
                    if add_s.isdigit() and int(add_s) >= need:
                        player.wallet += int(add_s)
                        player.wallet -= amount
                        self.dialogue.say("Shopkeeper", "Wallet top up and payment done.")
                        return True, "Wallet"
                return False, "Wallet"
        else:
            print("Invalid method.")
            return False, "Invalid"

    # ---------- Police call (explicit command) ----------
    def call_police_scene(self, reason="Dispute"):
        rude = random.random() < 0.5
        scam = random.random() < 0.5
        mood = "rude" if rude else "polite"
        self.dialogue.say("System", "Calling the police...")
        pause(1)
        if rude:
            self.dialogue.say("Shopkeeper", "You again? Pay or get out. I will twist the bill if I want.")
        if scam:
            self.dialogue.say("Shopkeeper", "There is a service fee. New rule. Pay 20% more.")
        pause(1)
        self.dialogue.say("Police", "We are here. What is the issue?")
        print("1: Explain the issue calmly\n2: Accuse shopkeeper of scam\n3: Stay silent")
        choice = input("Choose 1/2/3: ").strip()
        if choice == "1":
            self.dialogue.say("Customer", "Officer, there is a billing problem. Please check.")
            if scam or rude:
                self.dialogue.say("Police", "Shopkeeper, show records.")
                self.dialogue.say("Shopkeeper", "Records are clean.")
                if random.random() < 0.5:
                    self.dialogue.say("Police", "I see extra fee. Remove it.")
                    player.reputation += 5
                else:
                    self.dialogue.say("Police", "Looks fine. Both of you adjust.")
            else:
                self.dialogue.say("Police", "Nothing serious. Please be civil.")
        elif choice == "2":
            self.dialogue.say("Customer", "Officer, he tried to scam me.")
            if random.random() < 0.5:
                self.dialogue.say("Police", "We will fine the shop.")
                player.reputation += 3
            else:
                self.dialogue.say("Police", "Do you have proof?")
                pr = input("Do you have receipt? (yes/no): ").strip().lower()
                if pr == "yes":
                    self.dialogue.say("Police", "Ok. We will record this.")
                    player.reputation += 2
                else:
                    if player.flags.get("police_immunity"):
                        self.dialogue.say("Police", "We will let it go this time.")
                    else:
                        self.dialogue.say("Police", "No proof. Come to station.")
                        self.dialogue.say("System", "You have been sent to jail.")
                        self.dialogue.evaluate()
                        raise SystemExit
        else:
            self.dialogue.say("Customer", "...")
            self.dialogue.say("Police", "Then we will close this.")

    # ---------- Negotiation mini-game ----------
    def negotiate(self):
        self.dialogue.say("Shopkeeper", "Say a number. If I like it, I will cut your bill by that percent up to 10%.")
        num = ask_int("Your percent (0-10): ")
        if num is None or num < 0:
            print("No deal.")
            return 0
        num = min(10, num)
        success = random.random() < (0.4 + num/100.0)
        if success:
            self.dialogue.say("Shopkeeper", f"Fine. I allow extra {num}% off on the subtotal today.")
            return num/100.0
        else:
            self.dialogue.say("Shopkeeper", "No. Price stays.")
            return 0

# ============================ GAME FUNCTIONS ============================

def save_game(shop, cart):
    data = {
        "player": {
            "name": player.name,
            "reputation": player.reputation,
            "wallet": player.wallet,
            "loyalty_points": player.loyalty_points,
            "city": player.city,
            "health": player.health,
            "hunger": player.hunger,
            "inventory": player.inventory,
            "coupons": [vars(c) for c in player.coupons],
            "coupon_cost_total": player.coupon_cost_total,
            "flags": player.flags,
        },
        "shop": {
            "stock": shop.stock,
            "behaviour": shop.behaviour,
            "session_extra_sale": shop.session_extra_sale,
            "time_of_day": shop.time_of_day,
            "weather": shop.weather,
        },
        "cart": cart,
        "timestamp": now_str(),
        "version": VERSION,
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Game saved to {SAVE_FILE}")


def load_game():
    if not os.path.exists(SAVE_FILE):
        print("No save found.")
        return None
    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def apply_load(data, shop):
    p = data["player"]
    player.name = p["name"]
    player.reputation = p["reputation"]
    player.wallet = p["wallet"]
    player.loyalty_points = p["loyalty_points"]
    player.city = p["city"]
    player.health = p["health"]
    player.hunger = p["hunger"]
    player.inventory = p["inventory"]
    player.coupons = []
    for c in p["coupons"]:
        cc = Coupon(c["id"], c["price"], c["effect"])
        cc.redeemed = c["redeemed"]
        player.coupons.append(cc)
    player.coupon_cost_total = p["coupon_cost_total"]
    player.flags = p.get("flags", {})

    s = data["shop"]
    shop.stock = {int(k):v for k,v in s["stock"].items()}
    shop.behaviour = s["behaviour"]
    shop.session_extra_sale = s["session_extra_sale"]
    shop.time_of_day = s["time_of_day"]
    shop.weather = s["weather"]
    cart = {int(k):v for k,v in data["cart"].items()}
    print("Save loaded.")
    return cart


def travel(shop):
    print("Cities:")
    for name, cost in CITIES.items():
        print(f"- {name} (travel cost Rs.{cost})")
    dest = input("Where do you want to go?: ").strip()
    if dest in CITIES:
        cost = CITIES[dest]
        if player.wallet >= cost:
            player.wallet -= cost
            player.city = dest
            shop.time_of_day = random.choice(TIMES_OF_DAY)
            shop.weather = random.choice(WEATHERS)
            shop.behaviour = random.choice(list(BEHAVIOURS.keys()))
            print(f"You traveled to {dest}. It cost Rs.{cost}.")
        else:
            print("You do not have enough money.")
    else:
        print("No such place.")


def show_help():
    print("\nCommands:")
    print("/menu              -> show items")
    print("/buy <id> <qty>    -> add to cart")
    print("/remove <id> <qty> -> remove from cart")
    print("/cart              -> view cart")
    print("/search <word>     -> search item")
    print("/buycoupon         -> buy a sealed coupon")
    print("/buyallcoupons     -> buy several sealed coupons")
    print("/buyallitems       -> attempt to buy all stock (respecting stock)")
    print("/negotiate         -> try extra discount")
    print("/callpolice        -> call police with dynamic scene")
    print("/travel            -> move to another city")
    print("/save              -> save game")
    print("/load              -> load game")
    print("/checkout          -> go to billing")
    print("/help              -> this help\n")


# ============================ MAIN LOOP ============================
player = Player()
shop = Shop()
cart = {}
extra_negotiated_discount = 0.0

print(f"Welcome to {SHOP_NAME} – {VERSION}")
player.name = input("Enter your name: ").strip().title() or "Customer"
shop.greet()
shop.banner()
shop.display_menu()
show_help()

while True:
    if shop.all_sold_out() and not cart:
        shop.dialogue.say("Shopkeeper", "Everything is sold out. Come tomorrow.")
        break

    cmd = input("\n> ").strip()
    if not cmd:
        continue

    parts = cmd.split()
    base = parts[0].lower()

    if base == "/help":
        show_help()

    elif base == "/menu":
        shop.display_menu()

    elif base == "/search":
        if len(parts) < 2:
            print("Use: /search <word>")
        else:
            shop.search(" ".join(parts[1:]))

    elif base == "/buy":
        if len(parts) < 3:
            print("Use: /buy <id> <qty>")
            continue
        if not parts[1].isdigit() or not parts[2].isdigit():
            print("Use numbers for id and qty.")
            continue
        iid = int(parts[1])
        qty = int(parts[2])
        shop.add_to_cart(cart, iid, qty)

    elif base == "/remove":
        if len(parts) < 3:
            print("Use: /remove <id> <qty>")
            continue
        if not parts[1].isdigit() or not parts[2].isdigit():
            print("Use numbers for id and qty.")
            continue
        iid = int(parts[1])
        qty = int(parts[2])
        shop.remove_from_cart(cart, iid, qty)

    elif base == "/cart":
        if not cart and not player.coupons:
            print("Cart is empty.")
        else:
            print("\n-- Cart --")
            for iid, q in cart.items():
                print(f"{MENU[iid]} x{q} @Rs.{PRICES[iid]}")
            if player.coupon_cost_total > 0:
                print(f"Coupons purchased total: Rs.{player.coupon_cost_total}")
            if player.coupons:
                for c in player.coupons:
                    print(f"{c.label()} - Rs.{c.price} [{'used' if c.redeemed else 'sealed'}]")

    elif base == "/buycoupon":
        shop.buy_coupon()

    elif base == "/buyallcoupons":
        shop.buy_all_coupons()

    elif base == "/buyallitems":
        bought_any = False
        for iid in sorted(MENU.keys()):
            if iid == 9:
                continue
            qty = shop.stock[iid]
            if qty > 0:
                shop.add_to_cart(cart, iid, qty)
                bought_any = True
        if not bought_any:
            print("Nothing left to buy.")

    elif base == "/negotiate":
        extra_negotiated_discount = shop.negotiate()

    elif base == "/callpolice":
        shop.call_police_scene("User command")

    elif base == "/travel":
        travel(shop)
        shop.banner()

    elif base == "/save":
        save_game(shop, cart)

    elif base == "/load":
        data = load_game()
        if data:
            cart = apply_load(data, shop)
            shop.banner()
            shop.display_menu()

    elif base in ("/checkout", "no"):
        break

    else:
        print("Unknown command. Type /help.")

# ============================ BILLING PHASE ============================
if not cart and player.coupon_cost_total == 0:
    shop.dialogue.say("Shopkeeper", "You did not buy anything. Thank you for the visit.")
    shop.dialogue.evaluate()
    raise SystemExit

apply_gst = input("Do you want GST bill (18%)? (yes/no): ").strip().lower() == "yes"
used_coupon = None
if player.coupons:
    print("You have coupons:")
    for i, c in enumerate(player.coupons, start=1):
        print(f"{i}. {c.label()} - Rs.{c.price} [{'used' if c.redeemed else 'sealed'}]")
    use = input("Redeem one coupon now? (yes/no): ").strip().lower()
    if use == "yes":
        pick = input("Enter coupon number: ").strip()
        if pick.isdigit():
            idx = int(pick)
            if 1 <= idx <= len(player.coupons):
                used_coupon = player.coupons[idx-1]

bill = shop.compute_totals(cart, player.loyalty_points, apply_gst, used_coupon)

# apply negotiated discount on top of pre-tax
if extra_negotiated_discount > 0:
    cut = int(round(bill["pre_tax_total"] * extra_negotiated_discount))
    bill["pre_tax_total"] = max(0, bill["pre_tax_total"] - cut)
    bill["grand_total"] = bill["pre_tax_total"] + bill["gst_amount"]

# print bill
print("\n============================== FINAL BILL ==============================")
print(f"Shop       : {SHOP_NAME}")
print(f"Version    : {VERSION}")
print(f"Customer   : {player.name}")
print(f"Date/Time  : {now_str()}")
print("-----------------------------------------------------------------------")
for (iid, name, unit, qty, line) in bill["line_items"]:
    print(f"{name:<45} x{qty:<3}  @Rs.{unit:<4}  = Rs.{line}")
print("-----------------------------------------------------------------------")
print(f"Subtotal                         : Rs. {bill['base_subtotal']}")
print(f"Sale off                         : Rs. {bill['sale_discount']}")
print(f"Offer discounts                  : Rs. {bill['offer_discount']}")
if bill["secret_note"]:
    print(f"Secret note                      : {bill['secret_note']}")
if bill["secret_discount"]:
    print(f"Secret discount                  : Rs. {bill['secret_discount']}")
if bill["redeem_used"]:
    print(f"Loyalty redeemed                 : Rs. {bill['redeem_used']}")
print(f"Pre-tax total                    : Rs. {bill['pre_tax_total']}")
print(f"GST                              : Rs. {bill['gst_amount']}")
print("-----------------------------------------------------------------------")
print(f"TOTAL PAYABLE                    : Rs. {bill['grand_total']}")
print(f"Loyalty points earned            : {bill['points_earned']}")
print("=======================================================================\n")

# Payment
paid, method = shop.payment(bill["grand_total"])
if not paid:
    shop.dialogue.say("Shopkeeper", "You have not paid. One more chance.")
    try_again = input("Try payment again? (yes/no): ").strip().lower()
    if try_again == "yes":
        paid, method = shop.payment(bill["grand_total"])

if not paid:
    # Non-payment branch
    shop.dialogue.say("Shopkeeper", "I will call the police if you do not pay.")
    shop.call_police_scene("Non-payment")
    # final attempt
    paid, method = shop.payment(bill["grand_total"])
    if not paid:
        shop.dialogue.say("Police", "You refused to pay. Come to the station.")
        shop.dialogue.say("System", "You have been sent to jail.")
        shop.dialogue.evaluate()
        raise SystemExit

shop.dialogue.say("Shopkeeper", f"Thank you for the payment by {method}.")

# Wallet cashback for wallet method
if method == "Wallet":
    cb = int(round(bill["pre_tax_total"] * WALLET_CASHBACK_RATE))
    player.wallet += cb
    shop.dialogue.say("Shopkeeper", f"Cashback added to your wallet: Rs.{cb}.")

# secret cashback
if bill["cashback_flag"]:
    cb2 = int(round(bill["pre_tax_total"] * 0.10))
    player.wallet += cb2
    shop.dialogue.say("Shopkeeper", f"A secret reward was applied. Wallet +Rs.{cb2}.")

# police immunity flag
if bill["police_immunity"]:
    player.flags["police_immunity"] = True

# add loyalty
player.loyalty_points = bill["points_earned"]

# After-sale random events
r = random.random()
if r < 0.10:
    shop.dialogue.say("System", "Police raid in the area. Shops may close early tomorrow.")
elif r < 0.20:
    shop.dialogue.say("System", "Festival starts tomorrow. Prices will shift.")
elif r < 0.25:
    shop.dialogue.say("System", "Street fight in Black Alley. Travel may be unsafe.")

# Ending checks (very simple demo)
end = None
if player.reputation > 50 and player.wallet > 500:
    end = "Honored Customer Ending"
elif player.reputation < -50:
    end = "Outlaw Ending"

if end:
    print(f"\nENDING UNLOCKED: {end}")

shop.dialogue.say("Shopkeeper", "Thank you for shopping. Come again.")
shop.dialogue.evaluate()
