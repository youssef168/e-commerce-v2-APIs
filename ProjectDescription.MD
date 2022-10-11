# Mulit-Vendor E-commerce

---

# This Project Built With: Reactjs as frontend and django as backend

---

# Features:

# 1. Vendors:

## each vendor can publish and edit his product whenever he wants to! and each vendor has his own information and dashboard, here's a list of info that vendor should has:

### 1. Store Picture

### 2. Store Banner

### 2. Store Name

### 3. Location -> auto add or vendor can add it on his own

### 4. Phone Number

### 5. Average Rating -> auto added by the server not the vendor

# Vendor Specific Details And Settings:

## 1. Store Product Per Page: how many items will be implemented on each page, Included in settings section of the vendor

## 2. Steet of the vendor

## 3. city of the vendor

## 4. country of the vendor

## 5. state of the vendor

# settings and account information:

# NOTE: These data won't be used in any exernal operation and it just for showcase, in case this project has been salled out, there'll be other plans for sure

## 1. PayPal Account

## 2. Bank Transfer Info:

## 1. Account Holder

## 2. Account Type

## 3. Account Number

## 4. Bank Name

## 5. Bank Address

## 6. Bank IBAN

## 7. Bank Swift Code

# 2. Subscription:

## users can subscribe with some store (Vendor) and receive notification when they upload some new product or publish some blog

# 3. Send Messages To Some Store

# 4. Whishlist

## users can add products to thier whishlist and also move them to the cart

# 4. Review Product:

## users can review product and add thier rating into it

# 5. Analytics!!:

## admin has analytics board which gives him some features, here's list of features:

### 1. Keep Tracking of daily logged in users

# Security points:

## I did my best to secure this project as much as I could, so let's discuss what I've Done!

# httpOnly Cookies:

## we all know that when we store some data on the local storage will be accessible from external because any javascript code can access it but what if js itself cannot access it? that is exactly what I did! the sensitive data are not accessible from any js code, which means attackers cannot access it, only the server has permission to access it, let's know-how

## now when the user login into the website it should return the access and refresh token, which is important as much as password does! can you set the user's password in the local storage? definitely not! it's imposiblie, this how you should treat tokens! so there's something called httpOnly Cookies which is very awesome and helpful in this sitiuation! this soluation based on js codes are blocked to access it, why? because attackers can use js to access normal cookie like local storage and get all the data inside of it, while httpOnly cookies are not accessable from any js code, so how we'd get the token?

## good quistion, the server itself will set the cookies into response and will get it by request.COOKIES flag, so frontend clients are not resposible any more about sending authrize token to the server, because the server will check this automaticly!
