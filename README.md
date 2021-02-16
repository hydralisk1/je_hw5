# HW5
## 0. Repeat everything I coded during the class.
## 0. Read about waits.
## 0. Read about selenium exceptions: https://dzone.com/articles/selenium-webdriver-exceptions
## 0. Interview QQQQ! : Interview Q&A

## 1. Go over your code and remove sleep() wherever possible. 
Replace sleep() with wait.until if needed.

## 2. Make a test case with a loop. You can use https://www.amazon.com/gp/product/B07BJKRR25/ color selection or any other product page.
Create 1 test case that will loop through colors: it should click on each color and verify that color has been selected.
```done - /features/click_every_color.feature```

## 3.*[Not required]. Make a test case to verify that every product on the Wholefoods page has a text ‘Regular’ and a product name: https://www.amazon.com/wholefoodsdeals 
NOTE: ONLY USE BOTTOM SECTION:
```done - /features/wholefoods_products.feature```


## 4*[Not required]. Solve this kata 
https://www.codewars.com/kata/5f0ed36164f2bc00283aed07/train/python
```done``` - https://www.codewars.com/users/hydralisk1/completed_solutions

## 5**[Not required]. Amazon interview question:
Create a function that will take a string as an input and return the 1st non-unique letter of a string.
“Google” => “l”
“Amazon” => “m”
If there are no unique letters, return an empty string: “xoxoxo” => “”.
How would you test it? How would you handle edge cases?
```done - amazon_interview.py```