# Udacity-Unscramble-Computer-Science-Problems
Submission to Udacity's Unscramble Computer Science Problems

Run time analysis (Worst Case Big-O Notation) of your solution

Get Time Taken to run using : time python <filename>


- TASK 0 :
    Worse case complexity: O(1)
        Algorithm:
            get first data in list using index 0(complexity: O(1))
            get last data in list using index (length of list - 1) or (-1)(complexity: O(1))
            print resulting string to console(complexity: O(1))
        Time Taken to run:
            real    0m0.081s
            user    0m0.039s
            sys     0m0.032s

- TASK 1 
    Worst case complexity: O(n)
        Algorithm:
            initialise an empty set(complexity: O(1))
            map through calls and texts to update set(complexity: O(n))
            print resulting set length to console(complexity: O(1))
        Time Taken to run:
            real    0m0.107s
            user    0m0.045s
            sys     0m0.035s

- TASK 2
    Worse case complexity: O(n)
        Algorithm:
            initialise cummulative dictionary set(complexity: O(1))
            map through calls sets and update cummulative dictionary set if call was made in september 2016(complexity: O(n))
            print maximum key and value from dictionary set(complexity: O(1))
        Time Taken to run:
            real    0m0.091s
            user    0m0.052s
            sys     0m0.030s

- TASK 3 
    Worse case complexity: O(n)
        Algorithm:
            initialise an empty area codes set (complexity: O(1))
            map through calls sets and update area codes(complexity: O(n))
            print area code (complexity: O(1))
            get percentage (complexity: O(1))
            print percentage (complexity: O(1))
        Time Taken to run:
            real    0m0.078s
            user    0m0.041s
            sys     0m0.030s

- TASK 4 
    Worse case complexity: O(n)
        Algorithm:
            initialise an empty text and call checkers set(complexity: O(1))
            map through texts to set test checkers(complexity: O(n))
            map through calls to set call checkers(complexity: O(n))
            map through calls to update possible telemarketers using checkers generated above(complexity: O(n))
            print possible telemarketers (complexity: O(1))
        Time Taken to run:
            real    0m0.086s
            user    0m0.043s
            sys     0m0.030s