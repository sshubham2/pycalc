# SPDX-FileCopyrightText: 2023-present Shubhendu Shubham <s2.shubh2@gmail.com>
#
# SPDX-License-Identifier: MIT

class operations:
    
    def __init__(self) -> None:
        self.num1 : int
        self.num2 : int
        self.result : int
        
    def sum(self) -> int:
        self.num1 = int(input("First Number : "))
        self.num2 = int(input("Second Number : "))
        self.result = self.num1 + self.num2
        return self.result