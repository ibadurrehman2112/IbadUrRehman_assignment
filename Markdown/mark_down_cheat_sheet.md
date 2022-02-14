# 1- Headings
How to give headings in markdown files?
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5

# 2- Block of words

This is a normal text in markdown

> THis is a block of special text
>
> THis is a second line

# 3- Line breaks

This is a 40 days long course Data science with python.

This is a second line

This is a 40 days long course Data science with python.\
This is a second line

# 4- Combine two things
 
Block of codes

> ## Heading 2

# 5- Face of text

Bold 
Italic 
Bold and Italic

**Bold**
*XYZ*
***QWERT***
 or you can use these symbols
 _ (Underscore)

 _Bold_

_Italic_

> write in comments about Bold and Italic with underscore

# 6- Bullet points/ Lists

- Day-1
- Day-2
- Day-3
- Day-4
- Day-5
    - Day-5a
    - Day-5b
- Day-6

> __using *or#__

>Numbering of lists

1. Day1
2. Day2
3. Day3
1. Day4
    - Day4a
    - day4b
1. Day6

# 7- Line breaks or page breaks

This is page 1.
___
***
---
This is page 2.

# 8- Links and Hyperlinks

<https://help.ubuntu.com/>

[The playlist of python ka chilla is here](https://help.ubuntu.com/)

[Ubuntu help]:https://help.ubuntu.com/

This whole course is [here][Ubuntu help]

# 9- Images and figures with link 

To join me, please scan this QR:
[QR](qr_code.png)

> Task: how to comment out a markdown line? and its shorcut?

Online picture:

[Codanics](https://www.google.com/search?q=codanics&sxsrf=APq-WBuio6jtqkC8R6zL9utbB4KpDoNRcQ:1644515703960&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjxoPKy2vX1AhXCzIUKHT18D5sQ_AUoAnoECAEQBA&biw=1536&bih=662&dpr=1.25#imgrc=GRjVtCcWAILqOM)


# 10- Adding code or code blocks

To print a string use `print("Codanics")`
`print("Hello world")`

```python
x = 5+6
y = 3-2
z = x+y
print(z)
```

```C++
x = 5+6
y = 3-2
z = x+y
print(z)
```

```html
x = 5+6
y = 3-2
z = x+y
print(z)
```

> this code with show color according to R language syntax

```r
x = 5+6
y = 3-2
z = x+y
print(z)
```

# 11- Adding table

| species | petal_length | sepal_length |
| :------- | :------------: | ------------: |
| virginica |18.2 | 17.2 | 
| setosa | 25.5 | 26 |


# 12 - content

[1-Headings](#1--headings)\
[2- block-of-words](#2--block-of-words)\
[3- line break](#3--line-breaks)\
[4- combine-two-things](#4--combine-two-things)\
[5- face-of-text](#5--face-of-text)\
[6- bullet-points-lists](#6--bullet-points-lists)\
[7- line-breaks-or-page-breaks](#7--line-breaks-or-page-breaks)\
[8- links-and-hyperlinks](#8--links-and-hyperlinks)\
[9- images-and-figures-with-link](#9--images-and-figures-with-link)\
[10- adding-code-or-code-blocks](#10--adding-code-or-code-blocks)\
[11- adding-table](#11--adding-table)

# 13- Install extensions

**Sample Text**

**Bold**

_Italic_

[link](https://askubuntu.com/)

![Image](qr_code.png)

[Image](qr_code.png)

~~Image~~

```
code

```
<span style ="color:red">
"This text color is red"
</span>

# 15- Adding equations in MD

> In-line math

$this_{is}^{inline}$

> Math Block

$$ 
\int_0^\infty \frac{x^3}{e^x-1}\,dx
=\frac{\pi^4}{15}
$$

You can watch following linkfor more information: [MathJax](https://jupyterbook.org/content/math.html)