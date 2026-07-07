# 🚗 Vehicle Number Plate Format Validator

## 📌 Project Overview

The **Vehicle Number Plate Format Validator** is a Python-based application developed to validate Indian vehicle registration numbers according to the standard RTO format.

The program accepts a vehicle number, normalizes the input, validates each section of the registration number, and displays the corresponding state, district (RTO), series code, vehicle number, and an estimated registration sequence within the state.

This project was developed using Python Module 2 concepts such as strings, tuples, dictionaries, slicing, string methods, and conditional statements without using regular expressions.

---

# 📖 Problem Statement

An RTO portal must validate that a vehicle registration number follows the standard format consisting of:

* State Code
* District (RTO) Code
* Series Code
* Vehicle Number

The validator should:

* Accept correctly formatted vehicle numbers.
* Reject invalid registrations.
* Identify exactly which segment is invalid.
* Normalize user input by removing spaces and converting letters to uppercase.
* Validate the registration number without using regular expressions.

---

# 🎯 Objectives

* Validate Indian vehicle registration numbers.
* Verify every segment individually.
* Display meaningful error messages.
* Improve user experience by accepting lowercase letters and extra spaces.
* Provide additional information such as State and District names.

---

# 🛠 Technologies Used

* Python 3
* Strings
* Tuples
* Dictionaries
* String Slicing
* String Methods
* Conditional Statements
* Functions

---

# 📂 Number Plate Format

Example:

AP39AB1234

| Segment | Description         |
| ------- | ------------------- |
| AP      | State Code          |
| 39      | District / RTO Code |
| AB      | Series Code         |
| 1234    | Vehicle Number      |

---

# ⚙ Features

* Accepts vehicle registration number as input.
* Removes unnecessary spaces.
* Converts lowercase input to uppercase.
* Validates State Code.
* Validates District (RTO) Code.
* Validates Series Code.
* Validates Vehicle Number.
* Displays State Name.
* Displays District Name.
* Calculates the Series Order.
* Calculates the estimated vehicle registration order.
* Stops execution immediately when an invalid segment is detected.

---

# 🧠 Project Workflow

1. Read the vehicle number from the user.
2. Remove leading, trailing, and internal spaces.
3. Convert the input to uppercase.
4. Check whether the length is exactly 10 characters.
5. Validate the State Code.
6. Validate the District (RTO) Code.
7. Validate the Series Code.
8. Validate the Vehicle Number.
9. Calculate the Series Order.
10. Calculate the estimated vehicle registration order.
11. Display all information.

---

# 📊 Validation Rules

### State Code

* Must contain exactly 2 alphabetic characters.
* Must match a valid Indian State Code.

Example:

* AP
* TS
* KA

---

### District (RTO) Code

* Must contain exactly 2 digits.
* Must exist for the selected state.

Example:

* 39
* 10
* 23

---

### Series Code

* Must contain exactly 2 alphabetic characters.

Example:

* AA
* AB
* XY

---

### Vehicle Number

* Must contain exactly 4 digits.

Example:

* 0001
* 1234
* 9999

---

# 📈 Series Order Logic

Each series is converted into an order using the following logic:

```
First Letter = ord(letter1) - ord('A')
Second Letter = ord(letter2) - ord('A')

Series Order = (First Letter × 26) + Second Letter
```

Example:

| Series | Order |
| ------ | ----- |
| AA     | 0     |
| AB     | 1     |
| AC     | 2     |
| AZ     | 25    |
| BA     | 26    |
| BB     | 27    |

---

# 🚘 Vehicle Registration Order

The estimated vehicle registration order is calculated using:

```
Vehicle Position =
(Series Order × 9999) + Vehicle Number
```

Example:

```
Plate : AP39AB1234

Series Order : 1

Vehicle Position :
(1 × 9999) + 1234
= 11233
```

---

# ✅ Sample Output

Input:

```
Enter Vehicle Number:
ap 39 ab 1234
```

Output:

```
State : Andhra Pradesh
District : Tirupati (Additional RTO)
Series Code : AB
Vehicle Number : 1234

The number of the vehicle in the state is:
11233th vehicle
```

---

# ❌ Invalid Examples

Example 1

```
Input:
A139AB1234

Output:
Invalid State
```

Example 2

```
Input:
AP3AAB1234

Output:
Invalid RTO Code
```

Example 3

```
Input:
AP39121234

Output:
Invalid Series
```

Example 4

```
Input:
AP39AB12A4

Output:
Invalid Vehicle Number
```

---

# 📚 Python Concepts Used

* Functions
* Strings
* Tuples
* Dictionaries
* String Slicing
* String Methods
* Conditional Statements
* Input and Output
* Return Statements

---

# 🚀 Future Enhancements

* Support Bharat Series (BH) registration numbers.
* Validate temporary registration numbers.
* Add support for VIP registration numbers.
* Develop a graphical user interface (GUI).
* Connect to a database for real-time RTO validation.
* Export validation reports.

---


