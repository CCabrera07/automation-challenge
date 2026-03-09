Consigna: En un editor de textos a elección, escriba los casos de pruebas que considere necesarios para validar todos los escenarios posibles sobre las funcionalidades “Inicio de sesión” y “Agregado de productos al carrito de compras” de la web https://www.saucedemo.com/
Los casos de pruebas también se encuentran en [Notion](https://historical-wedge-9f5.notion.site/31dd42f3023b80be866ace0ef0e18607?v=31dd42f3023b81d3a1d2000c29407dd7&source=copy_link): https://historical-wedge-9f5.notion.site/31dd42f3023b80be866ace0ef0e18607?v=31dd42f3023b81d3a1d2000c29407dd7&source=copy_link

# Feature: Test Login

## TC 001
**Title:** Successful login with valid credentials.
**Priority:** High.

**Preconditions:** 
1. The user is on the SauceDemo login page.
2. The standard_user is active.

**Test data**
Username: standard_user
Password: secret_sauce

**Steps**
1. Navigate https://www.saucedemo.com/
2. Enter standard_user in the Username field. 
3. Enter secret_sauce in the Password field. 
4. Click the Login button.

**Expected result:**
1. The user is successfully redirected to the **inventory page**.
2. The list of products is displayed.
3. The URL contains **/inventory.html**

TC: [NOTION](https://www.notion.so/CP-001-Generar-una-reserva-ingresando-datos-v-lidos-31dd42f3023b81e2a77fd9cecf27bcba) 

## TC 002 
**Title:** Test Validate error message when logging in with an incorrect password.
**Priority:** High.

**Preconditions:** 
1. The user is on the SauceDemo login page.
 
**Test data**
Username: standard_user
Password: wrong_password

**Steps**
1. Navigate to https://www.saucedemo.com/
2. Enter standard_user in the Username field.
3. Enter wrong_password in the Password field.
4. Click the Login button.
5. An error message is displayed indicating "Epic sadface: Username and password do not match any user in this service".

**Expected result:**
1. The system denies access.
2. An error message is displayed indicating that the username or password is invalid.
3. The user remains on the login page.

TC: [NOTION](https://www.notion.so/TC-002-Test-Validate-error-message-when-logging-in-with-an-incorrect-password-31ed42f3023b808b82e8d737e4dfff0b) 

## TC 003
**Title:** Validate error message when attempting login with empty fields.
**Priority:** High.

**Preconditions:** 
1. The user is on the SauceDemo login page.
 
**Test data**
Username: empty
Password: empty

**Steps**
1. Navigate to https://www.saucedemo.com/
2. Leave the Username field empty.
3. Leave the Password field empty.
4. Click the Login button.

**Expected result:**
1. The system denies access.
2. An error message is displayed indicating that the Epic sadface: Username is required.
3. The user remains on the login page.

TC: NOTION https://www.notion.so/TC-003-Validate-error-message-when-attempting-login-with-empty-fields-31ed42f3023b804aa561db5443f34c18

## TC 004
**Title:** Validate that a locked user cannot log in
**Priority:** High.

**Preconditions:** 
1. The user is on the SauceDemo login page.
2. The user locked_out_user exists and is locked.

**Test data**
Username: standard_user
Password: secret_sauce

**Steps**
1. Navigate to https://www.saucedemo.com/
2. Enter locked_out_user in the Username field.
3. Enter secret_sauce in the Password field.
4. Click the Login button.

**Expected result:**
1. The system denies access. 
2. An error message is displayed indicating that the user is locked. 
3. The user remains on the login page.

TC NOTION: https://www.notion.so/TC-004-Validate-that-a-locked-user-cannot-log-in-31ed42f3023b8055bea9dc3c5c8c37c3

## TC 005
**Title:** Validate error message when entering only username without password.
**Priority:** Medium.

**Preconditions:** 
1. The user is on the SauceDemo login page.

**Test data**
Username: standard_user
Password: secret_sauce

**Steps**
1. Navigate to https://www.saucedemo.com/
2. Enter standard_user in the Username field. 
3. Leave the Password field empty. 
4. Click the Login button.

**Expected result:**
1. The system denies access. 
2. An error message is displayed indicating that the Password field is required. 
3. The user remains on the login page.

TC NOTION:

# Feature: Add Products to Cart
## TC 006
**Title:** Add a product to the cart from the inventory page.
**Priority:** High.

**Preconditions:** 
1. The user has successfully logged in with valid credentials.
2. The user is on the inventory page

**Test data**
Product: Sauce Labs Backpack.

**Steps**
1. Log in with valid credentials. 
2. Locate the product Sauce Labs Backpack. 
3. Click the Add to cart button for the product.

**Expected result:**
1. The product is successfully added to the cart. 
2. The cart icon displays a badge with value 1. 
3. The button changes from Add to cart to Remove.

## TC 007
**Title:** Validate that the added product appears in the cart.
**Priority:** High.

**Preconditions:** 
1. The user is logged in.
2. At least one product has been added to the cart.
 
**Test data**
Product: Sauce Labs Backpack.

**Steps**
1. Log in with valid credentials.
2. Add Sauce Labs Backpack to the cart.
3. Click the cart icon.

**Expected result:**
1. The user is redirected to the cart page.
2. The product Sauce Labs Backpack is displayed in the cart.
3. The product name, description, and price are correct

## TC 008
**Title:** Add multiple products to the cart.
**Priority:** High.

**Preconditions:** 
1. The user is logged in.
2. The user is on the inventory page.

**Test data**
Product 1: Sauce Labs Backpack
Product 2: Sauce Labs Bike Light

**Steps**
1. Log in with valid credentials.
2. Add Sauce Labs Backpack to the cart.
3. Add Sauce Labs Bike Light to the cart

**Expected result:**
1. Both products are successfully added.
2. The cart badge displays the value 2.
3. Both buttons change to Remove.

## TC 009
**Title:** Remove a product from the cart from the inventory page.
**Priority:** Medium.

**Preconditions:** 
1. The user is logged in.
2. A product has been added to the cart.
 
**Test data**
Product: Sauce Labs Backpack

**Steps**
1. Log in with valid credentials.
2. Add Sauce Labs Backpack to the cart.
3. Click the Remove button.

**Expected result:**
1. The product is successfully removed from the cart.
The cart badge disappears or decreases accordingly.
The button changes back to Add to cart. 

## TC 010
**Title:** Validate that the cart retains added products when navigating to the cart view.
**Priority:** Medium.

**Preconditions:** 
1. The user is logged in.
2. Products have been added to the cart.
 
**Test data**
Product: Sauce Labs Backpack

**Steps**
1. Log in with valid credentials.
2. Add Sauce Labs Backpack to the cart.
3. Click the cart icon.

**Expected result:**
1. The previously added product remains in the cart.
2. The number of displayed products matches the number added.

## TC 011
**Title:** Validate empty cart when no products are added.
**Priority:** Low.

**Preconditions:** 
1. The user is logged in.
2. No products have been added to the cart
 
**Test data**
N/A

**Steps**
1. Log in with valid credentials.
2. Click the cart icon without adding any products

**Expected result:**
1. The user is redirected to the cart page.
2. No products are listed in the cart.
3. The cart badge is not displayed.
