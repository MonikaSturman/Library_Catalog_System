# Library Management System

This project implements a library management system in Python, allowing users to manage library items, membership and borrowing activities. The system includes classes for different 
types of library items(e.g., books, DVDs), membership management and interactions with the library catalog.

_**Features:**_

- LibraryItem Class: Base class representing generic library items with attributes like title, item ID, and availability status. Derived classes (e.g., Book, DVD) inherit from this class and add specific properties and behaviours.
- Book Class: Represents books in the library with attributes such as author, ISBN, and borrow-related methods (borrow_book, return_book).
- DVD Class: Represents DVDs in the library with attributes like director, release year, and borrow-related methods (borrow_dvd, return_dvd).
- LibraryMembership Class: Manages library members, including attributes for member ID, name, contact info, borrowed items, and membership status. Provides methods for borrowing and returning items, membership renewal, and status checks.
- Usage Example: Demonstrates how to create library items, manage memberships, borrow and return items, and check membership status.






