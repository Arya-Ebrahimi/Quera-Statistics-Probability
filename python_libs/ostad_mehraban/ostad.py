import numpy as np

grades = np.array([ 3. , 17. ,  6.5,  0.5,  8. ,  6.5, 19. , 13.5,  2.5, 17. , 19. ,
       19.5, 13. ,  0. ,  6. ,  0.5,  9.5, 13.5, 16. ,  2.5, 10.5,  8. ,
       10. , 15.5,  7.5,  0. ,  1. , 10.5,  2. , 11. ,  3. , 14. ,  3.5,
       18.5, 13. ,  1. , 14.5, 15. ,  1. , 15.5,  1.5,  2. ,  3.5,  6.5,
        2.5, 14.5, 11.5,  8. ,  0. ,  5.5,  0.5, 20. ,  5. ,  0.5, 17.5,
       17.5, 17.5, 15. ,  4.5, 17. , 18. , 10. ,  8.5, 14. , 18.5, 19.5,
       16. ,  8.5,  0. ,  9.5,  6. ,  2. ,  5. ,  9.5,  4. ,  4. ,  1. ,
        8. , 18.5, 18. , 15.5,  4.5,  1.5, 20. ,  0.5, 19. ,  4. ,  9.5,
       13. , 10. ,  3.5,  1.5,  6.5,  0.5, 11.5, 17. , 13.5, 11.5, 13. ,
       13. ])

for i in range(0, grades.size) : 
    if (grades[i] < 7) :
        grades[i] = grades[i]/10 + 9

    else :
        grades[i] = -0.0047 * pow(grades[i], 2) + 0.9571 * grades[i] + 3.5333
        
    if (grades[i] > 20) :
        grades[i] = 20

top_grades = grades[grades >= 17]

five_samples = top_grades [0: 5]