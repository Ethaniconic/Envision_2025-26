# Test Cases for Grey Market Detection Model
## Based on Final-snapdeal-dataset.csv

---

## TEST CASE SUMMARY
Total Test Cases: 30
Legitimate Products: 15
Grey Market Products: 15

---

## CATEGORY 1: WATCH PRODUCTS (Legitimate)

### Test Case 1: Popular Watch - High Reviews
**Input:**
- Product_Title: "EMPERO - Silver Stainless Steel Analog Men's Watch"
- Selling_Price: 311.0
- MRP: 1299.0
- Discount_Pct: 76.1
- Review_Count: 49

**Expected Output:** Legitimate (0)
**Reasoning:** Authorized seller status, reasonable review count, standard discount pattern

---

### Test Case 2: Mid-Range Watch with Good Reviews
**Input:**
- Product_Title: "PIRASO Silver Stainless Steel Analog Men's Watch"
- Selling_Price: 272.0
- MRP: 999.0
- Discount_Pct: 72.8
- Review_Count: 384

**Expected Output:** Legitimate (0)
**Reasoning:** High review count (384), consistent with known legitimate patterns, authorized seller

---

### Test Case 3: Premium Watch - Standard Discount
**Input:**
- Product_Title: "Renaissance Traders Gold Metal Analog Men's Watch"
- Selling_Price: 378.0
- MRP: 1299.0
- Discount_Pct: 70.9
- Review_Count: 603

**Expected Output:** Legitimate (0)
**Reasoning:** Very high review count (603), typical authorized seller pricing, strong indicator of legitimacy

---

### Test Case 4: Fashion Watch - Multiple Units in Stock
**Input:**
- Product_Title: "Shivark Black Silicon Analog Men's Watch"
- Selling_Price: 223.0
- MRP: 999.0
- Discount_Pct: 77.7
- Review_Count: 1068

**Expected Output:** Legitimate (0)
**Reasoning:** Extremely high review count (1068) indicates popular, authentic product

---

### Test Case 5: Basic Watch - Moderate Reviews
**Input:**
- Product_Title: "Fadiso Fashion Gold Stainless Steel Analog Men's Watch"
- Selling_Price: 308.0
- MRP: 1499.0
- Discount_Pct: 79.5
- Review_Count: 106

**Expected Output:** Legitimate (0)
**Reasoning:** Reasonable review count, known brand from authorized seller

---

## CATEGORY 2: WATCH PRODUCTS (Grey Market/Suspicious)

### Test Case 6: Luxury Watch with Extreme Discount
**Input:**
- Product_Title: "Om Collection - Brown Leather Analog Men's Watch"
- Selling_Price: 323.0
- MRP: 1799.0
- Discount_Pct: 82.0
- Review_Count: 64

**Expected Output:** Grey Market (1)
**Reasoning:** High discount (82%), low review count for premium item, suspicious pattern

---

### Test Case 7: Premium Watch - Suspiciously Low Reviews
**Input:**
- Product_Title: "Versatile - Black Stainless Steel Analog Men's Watch"
- Selling_Price: 263.0
- MRP: 1699.0
- Discount_Pct: 84.5
- Review_Count: 7

**Expected Output:** Grey Market (1)
**Reasoning:** Very high discount (84.5%) with extremely low reviews (7) - clear grey market indicator

---

### Test Case 8: High-End Watch with Extreme Discount and No Reviews
**Input:**
- Product_Title: "Lorenz Brown Leather Analog Men's Watch"
- Selling_Price: 381.0
- MRP: 1999.0
- Discount_Pct: 80.9
- Review_Count: 96

**Expected Output:** Grey Market (1)
**Reasoning:** 80%+ discount on premium item, pattern matches suspicious sellers

---

### Test Case 9: Designer Watch - Suspicious Pricing
**Input:**
- Product_Title: "FORNAX - Silver Stainless Steel Analog Men's Watch"
- Selling_Price: 272.0
- MRP: 1699.0
- Discount_Pct: 84.0
- Review_Count: 514

**Expected Output:** Grey Market (1)
**Reasoning:** High discount (84%) despite having reviews, inconsistent with legitimate patterns

---

### Test Case 10: Premium Watch - Very Few Reviews
**Input:**
- Product_Title: "EEWHI Black Brass Analog Men's Watch"
- Selling_Price: 380.0
- MRP: 1999.0
- Discount_Pct: 81.0
- Review_Count: 24

**Expected Output:** Grey Market (1)
**Reasoning:** 81% discount on luxury watch with minimal reviews (24)

---

## CATEGORY 3: SHOE PRODUCTS (Legitimate)

### Test Case 11: Kids Shoes - Good Sales Volume
**Input:**
- Product_Title: "Bunnies - Red Boy's LED Shoes ( 1 Pair )"
- Selling_Price: 292.0
- MRP: 499.0
- Discount_Pct: 41.5
- Review_Count: 274

**Expected Output:** Legitimate (0)
**Reasoning:** Moderate discount (41.5%), high review count (274), genuine product

---

### Test Case 12: Kids Sneakers - Popular Item
**Input:**
- Product_Title: "NEOBABY - Orange Boy's LED Shoes ( 1 Pair )"
- Selling_Price: 294.0
- MRP: 999.0
- Discount_Pct: 70.6
- Review_Count: 43

**Expected Output:** Legitimate (0)
**Reasoning:** Standard discount for kids' shoes, reasonable reviews

---

### Test Case 13: Kids Shoes - Branded Product
**Input:**
- Product_Title: "ASIAN - Blue Boy's Sneakers ( 1 Pair )"
- Selling_Price: 480.0
- MRP: 1199.0
- Discount_Pct: 60.0
- Review_Count: 9

**Expected Output:** Legitimate (0)
**Reasoning:** Recognized brand, standard discount range

---

### Test Case 14: Premium Kids Shoes - Multiple Reviews
**Input:**
- Product_Title: "Bersache - Orange Boy's LED Shoes ( 1 Pair )"
- Selling_Price: 493.0
- MRP: 1999.0
- Discount_Pct: 75.3
- Review_Count: 216

**Expected Output:** Legitimate (0)
**Reasoning:** High review count (216), popular branded item

---

### Test Case 15: Kids Footwear - Bulk Purchase
**Input:**
- Product_Title: "NEOBABY - MultiColor Boy's Casual Shoes ( 2 Pair )"
- Selling_Price: 294.0
- MRP: 1999.0
- Discount_Pct: 85.3
- Review_Count: 46

**Expected Output:** Legitimate (0)
**Reasoning:** Bulk purchase (2 pairs) justifies higher discount, good reviews (46)

---

## CATEGORY 4: SHOE PRODUCTS (Grey Market/Suspicious)

### Test Case 16: Kids Shoes - Vague Description
**Input:**
- Product_Title: "NEOBABY Casual Shoes for Kids Boys and Girls"
- Selling_Price: 213.0
- MRP: 999.0
- Discount_Pct: 78.7
- Review_Count: 119

**Expected Output:** Legitimate (0)
**Reasoning:** Despite vague title, high review count (119) suggests authenticity

---

### Test Case 17: Premium Shoe - No Reviews
**Input:**
- Product_Title: "Liberty - White Boy's Sneakers ( 1 Pair )"
- Selling_Price: 857.0
- MRP: 2199.0
- Discount_Pct: 61.0
- Review_Count: 0

**Expected Output:** Legitimate (0)
**Reasoning:** New product with no reviews yet, but reasonable discount

---

### Test Case 18: Budget Shoe - Minimal Reviews
**Input:**
- Product_Title: "Campus - Grey Boy's Sneakers ( 1 Pair )"
- Selling_Price: 400.0
- MRP: 749.0
- Discount_Pct: 46.6
- Review_Count: 3

**Expected Output:** Legitimate (0)
**Reasoning:** Budget product, low MRP justifies few reviews

---

### Test Case 19: Premium Shoes - Suspicious Pricing Pattern
**Input:**
- Product_Title: "Liberty - Grey Boy's Sneakers ( 1 Pair )"
- Selling_Price: 916.0
- MRP: 1099.0
- Discount_Pct: 16.7
- Review_Count: 2

**Expected Output:** Legitimate (0)
**Reasoning:** Low discount unusual but could be premium positioning

---

### Test Case 20: Multi-Pair Bundle - Very Few Reviews
**Input:**
- Product_Title: "Fabbmate - Pink Boy's LED Shoes ( 2 Pairs )"
- Selling_Price: 522.0
- MRP: 1499.0
- Discount_Pct: 65.2
- Review_Count: 0

**Expected Output:** Legitimate (0)
**Reasoning:** Bundle product, no reviews is acceptable for new listings

---

## CATEGORY 5: EDGE CASES & REALISTIC SCENARIOS

### Test Case 21: Designer Watch - Extreme Red Flags
**Input:**
- Product_Title: "ROLEX Submariner Replica High Quality"
- Selling_Price: 5000.0
- MRP: 350000.0
- Discount_Pct: 98.6
- Review_Count: 5

**Expected Output:** Grey Market (1)
**Reasoning:** 98.6% discount on luxury item, extremely suspicious

---

### Test Case 22: Mid-Range Watch - Legitimate
**Input:**
- Product_Title: "CHARLIEKEEN Black Metal Analog Men's Watch"
- Selling_Price: 476.0
- MRP: 1999.0
- Discount_Pct: 76.2
- Review_Count: 13

**Expected Output:** Legitimate (0)
**Reasoning:** Authorized seller, reasonable discount, newer product

---

### Test Case 23: Premium Watch - High Reviews Legitimacy Signal
**Input:**
- Product_Title: "Renaissance Traders - Black Metal Digital Men's Watch"
- Selling_Price: 378.0
- MRP: 999.0
- Discount_Pct: 62.2
- Review_Count: 468

**Expected Output:** Legitimate (0)
**Reasoning:** Very high review count (468) is strongest legitimacy indicator

---

### Test Case 24: Watch with Moderate Discount - Suspicious
**Input:**
- Product_Title: "Reboot Silver Stainless Steel Analog Men's Watch"
- Selling_Price: 278.0
- MRP: 1449.0
- Discount_Pct: 80.8
- Review_Count: 84

**Expected Output:** Grey Market (1)
**Reasoning:** High discount (80.8%) pattern characteristic of grey market

---

### Test Case 25: Popular Brand - Clear Legitimate
**Input:**
- Product_Title: "Harbor Black Silicon Analog-Digital Men's Watch"
- Selling_Price: 431.0
- MRP: 1999.0
- Discount_Pct: 78.4
- Review_Count: 50

**Expected Output:** Legitimate (0)
**Reasoning:** Recognized brand, reasonable review count

---

### Test Case 26: Luxury Item - Extreme Discount Warning
**Input:**
- Product_Title: "Om Collection DIGIARMY Rubber Digital Men's Watch"
- Selling_Price: 293.0
- MRP: 1799.0
- Discount_Pct: 83.7
- Review_Count: 12

**Expected Output:** Grey Market (1)
**Reasoning:** 83.7% discount, very low reviews for electronics

---

### Test Case 27: Standard Watch - Typical Pattern
**Input:**
- Product_Title: "HMXT Brown Leather Analog Men's Watch"
- Selling_Price: 292.0
- MRP: 999.0
- Discount_Pct: 70.8
- Review_Count: 128

**Expected Output:** Legitimate (0)
**Reasoning:** Consistent with legitimate authorized seller patterns

---

### Test Case 28: Kids Shoes - Bulk Buy Scenario
**Input:**
- Product_Title: "ICONIC ME - Multicolor Boy's Sneakers ( 1 Pair )"
- Selling_Price: 481.0
- MRP: 1299.0
- Discount_Pct: 63.0
- Review_Count: 14

**Expected Output:** Legitimate (0)
**Reasoning:** Branded product, reasonable discount

---

### Test Case 29: Children's Footwear - High Review Count
**Input:**
- Product_Title: "BUNNIES Baby Boys LED Leight Indian Walking Shoes (5 Years to 13 Years)"
- Selling_Price: 322.0
- MRP: 599.0
- Discount_Pct: 46.2
- Review_Count: 140

**Expected Output:** Legitimate (0)
**Reasoning:** Very high review count (140), popular children's brand

---

### Test Case 30: Sports Shoes - Premium with Good Reviews
**Input:**
- Product_Title: "Liberty - Blue Boy's Ethnic Shoes ( 1 Pair )"
- Selling_Price: 365.0
- MRP: 799.0
- Discount_Pct: 54.3
- Review_Count: 9

**Expected Output:** Legitimate (0)
**Reasoning:** Premium brand positioning, reasonable discount

---

## SUMMARY STATISTICS OF TEST CASES

### By Category:
- Watches (Legitimate): 5 test cases
- Watches (Grey Market): 5 test cases
- Shoes (Legitimate): 5 test cases
- Shoes (Grey Market): 0 test cases (shoes dataset shows mostly legitimate)
- Edge Cases & Mixed: 10 test cases

### Expected Distribution:
- Legitimate Products: 20 cases
- Grey Market Products: 10 cases

### Key Indicators Used:

**Legitimate Indicators:**
✅ Review count > 50
✅ Discount 40-80%
✅ Known brands/authorized sellers
✅ Multiple sales/bulk purchases
✅ Reasonable MRP ranges

**Grey Market Indicators:**
⚠️ Discount > 80%
⚠️ Review count < 25
⚠️ Luxury items at extreme discounts (>90%)
⚠️ Vague product descriptions
⚠️ Suspicious seller patterns
⚠️ Extreme MRP-to-selling price ratios (>95% off)

---

## USAGE INSTRUCTIONS

### Running Test Cases:
```bash
# Execute the test_models.py script which uses similar test data
python test_models.py

# Or use in Streamlit app:
streamlit run app.py
```

### Interpreting Results:
- **Confidence Score**: Higher % indicates stronger model confidence
- **Both Models Agree**: More reliable prediction
- **Models Disagree**: Review manually with pricing context

---

## NOTES FOR TESTING

1. **Review Count Context**: Very important signal - legitimate products accumulate reviews over time
2. **Discount Patterns**: 80%+ discounts are red flags except for specific categories
3. **Product Categories**: Watches show more grey market activity than shoes in this dataset
4. **MRP Realism**: Extreme MRP values (>₹10,000 discounted to <₹500) are suspicious
5. **Seasonal Factors**: High discounts during festivals may be legitimate

