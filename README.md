# 🐍 Python Number & Digit Manipulation Practice

## 📌 About This Repository

This repository contains my Python coding practice focused on **number manipulation, list operations, sorting, loops, indexing, and mathematical calculations**.

I solved practice problems step by step to improve my logical thinking, problem-solving skills, and Python fundamentals as part of my journey toward learning Data Structures and Algorithms (DSA).

## 🎯 Concepts Practiced

- Converting integers into lists of digits using `str()` and list comprehension.
- Sorting lists using `.sort()`.
- Accessing list elements using positive and negative indexing.
- Iterating through lists using `for` loops and `range()`.
- Performing multiplication, addition, and subtraction.
- Using variables and accumulators to calculate results.

## 🧩 Problems Solved

### 1. Product of the Two Largest Digits

Find the product of the two largest digits in a number.

**Example:**
```python
n = 5831
# Largest digits: 8 and 5
# Product: 8 * 5 = 40
```

### 2. Sum of the Two Largest Digits

Find the sum of the two largest digits.

**Example:**
```python
n = 4629
# Largest digits: 9 and 6
# Sum: 9 + 6 = 15
```

### 3. Product of the Two Smallest Digits

Find the product of the two smallest digits.

**Example:**
```python
n = 5831
# Smallest digits: 1 and 3
# Product: 1 * 3 = 3
```

### 4. Difference Between the Two Largest Digits

Find the difference between the largest and second-largest digits.

**Example:**
```python
n = 5831
# Largest digits: 8 and 5
# Difference: 8 - 5 = 3
```

### 5. Maximum Product of Three Digits

Find the product of the three largest digits.

**Example:**
```python
n = 4629
# Largest digits: 9, 6, and 4
# Product: 9 * 6 * 4 = 216
```

### 6. Maximum Product of Two Digits

Find the product of the two largest digits.

**Example:**
```python
n = 5831
# Largest digits: 8 and 5
# Product: 8 * 5 = 40
```

## 💻 Python Techniques Used

### Convert a Number into Digits
```python
n = 5831
digits = [int(d) for d in str(n)]
print(digits)
```

### Sort the Digits
```python
digits.sort()
```

### Select the Last Two Elements
```python
for i in range(len(digits) - 2, len(digits)):
    print(digits[i])
```

### Calculate a Product
```python
total = 1
for i in range(len(digits) - 2, len(digits)):
    total *= digits[i]
```

## 📚 What I Learned

- How to break a number into individual digits.
- How sorting helps identify the smallest and largest elements.
- How list indexing works.
- How `range()` controls the number of loop iterations.
- Why multiplication accumulators start at `1` and addition accumulators start at `0`.
- How to approach coding problems step by step.

## 🚀 Future Goals

- Practice more Python coding problems.
- Learn how to solve problems without sorting.
- Improve time and space complexity.
- Start learning DSA concepts such as arrays, strings, searching, and sorting algorithms.
- Prepare for technical interviews.

## 👨‍💻 About Me

I am a Computer Science and Engineering student learning Python and strengthening my problem-solving skills through consistent coding practice.

**Learning one concept at a time, one problem at a time!** 💪

---

⭐ This repository documents my Python learning journey. Suggestions and feedback are welcome.
