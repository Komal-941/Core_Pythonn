{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d091a7d5-da3f-43c1-9b41-e1bb4bc986a0",
   "metadata": {},
   "source": [
    "# IF\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d35fc6fe-3268-496c-9f9c-c45e11e87e86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Invalid\n"
     ]
    }
   ],
   "source": [
    "if 4<3:\n",
    "    print('komal')            #as condition failed it will ingnore the block \n",
    "    print('sopan')\n",
    "    print('shelar') \n",
    "    \n",
    "print(\"Invalid\")                      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e12d3477-e3ba-4572-a6b6-efd7effd6795",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter you age: 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "28\n"
     ]
    }
   ],
   "source": [
    "if 1 < 3:\n",
    "    a = eval((input(\"enter you age:\")))\n",
    "    b = 23\n",
    "    c = a+b\n",
    "    print(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "396fb2f4-9431-4c6e-b42e-4a83cf489ea5",
   "metadata": {},
   "source": [
    "# if-else\n",
    "- if above condition failed then the else block will execute automatically\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "a5507a6c-5d72-4667-943f-9b8d20dd570e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "1sem perce: 76.3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Passed\n"
     ]
    }
   ],
   "source": [
    "a = eval(input(\"1sem perce:\")) \n",
    "\n",
    "if  a>60:               #condn successed  ; so the main block  excecuted \n",
    "    print(\"Passed\") \n",
    "else:\n",
    "    print(\"Failed\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "cbdcbb15-4451-4f46-b682-b2c8b1fa1732",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your Pin 8790\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pin Mismatched\n"
     ]
    }
   ],
   "source": [
    "ATM = 8970  \n",
    "\n",
    "Pin = eval(input(\"enter your Pin\"))\n",
    "\n",
    "if Pin==ATM:\n",
    "    print(\"enter the withdrawl amount\") \n",
    "\n",
    "else:\n",
    "    print(\"Pin Mismatched\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e52e244-7cf4-4eea-9d09-a83c5e702711",
   "metadata": {},
   "source": [
    "# if-elif \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "d114fb40-1d9e-4cc0-baf5-0bbacef53059",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 45\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Eligible for Re-exam\n"
     ]
    }
   ],
   "source": [
    "Aggregate = eval(input()) \n",
    "\n",
    "if Aggregate>85:               #if the main block condn failed the it will go for the next condition i.e, 1 elif\n",
    "    print(\"First Class\") \n",
    "#1 elif\n",
    "elif Aggregate>70:\n",
    "    print(\"Second Class\")       #if the 1 elif condn failed the it will go for the next condition i.e, 2 elif\n",
    "#2 elif       \n",
    "elif Aggregate>65:\n",
    "    print(\"All Clear\")            #if the 2 elif condn failed the it will go for the next condition i.e, else \n",
    "    \n",
    "else:\n",
    "    print(\"Eligible for Re-exam\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "7282a935",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Grades receieved: 93.77\n",
      "students name: Sk\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sk got A Grade\n"
     ]
    }
   ],
   "source": [
    "#write a program to print grades of student, if marks>90 as a A grade ,if marks>70 as grade B, else Failed \n",
    "\n",
    "marks = eval(input(\"Grades receieved:\"))\n",
    "name = input(\"students name:\") \n",
    "\n",
    "if marks>90:\n",
    "    print(name,\"got A Grade\") \n",
    "\n",
    "elif marks>70:\n",
    "    print(name,\"got B Grade\")\n",
    "\n",
    "else:\n",
    "    print(\"Failed\") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "9c5a1eb2-1186-4a8c-be55-b4de7dfc4233",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "assignments done : 0,1,2,3 : 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "all work has been done\n"
     ]
    }
   ],
   "source": [
    "prompt = eval(input(\"assignments done : 0,1,2,3 :\")) \n",
    "\n",
    "if prompt ==0:\n",
    "    print(\"3 assignmnets pending\")\n",
    "\n",
    "elif prompt ==1:\n",
    "    print(\"2 assignments pending\") \n",
    "\n",
    "elif prompt==2:\n",
    "    print(\"1 more assignment pending\") \n",
    "\n",
    "elif prompt==3:\n",
    "    print(\"all work has been done\") \n",
    "\n",
    "else:\n",
    "    print(\"Something went wrong ; check for the count\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d05ffcfc-baac-46f0-9978-fe8312b35db5",
   "metadata": {},
   "source": [
    "# nested if \n",
    "\n",
    "- one more if - else - elif in existing if condn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "9b621168-274a-472c-8e2a-3e89ff453a1b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter your pin : 3456\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pin doesn't matched\n"
     ]
    }
   ],
   "source": [
    "pin = 2354\n",
    "balance = 30000\n",
    "\n",
    "entered_pin = eval(input(\"enter your pin :\")) \n",
    "\n",
    "if entered_pin == pin:\n",
    "    withdraw = int(input(\"enter the amount:\")) \n",
    "    if withdraw < balance:\n",
    "        print(\"transaction proceed\") \n",
    "    else:\n",
    "        print(\"insufficient balance\")\n",
    "\n",
    "\n",
    "else:\n",
    "    print(\"Pin doesn't matched\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ce7cb18-fef2-4c5b-a308-f7d388d19ef4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
