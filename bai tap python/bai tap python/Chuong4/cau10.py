import time
import os

# Hàm xóa màn hình (giúp mỗi hình xuất hiện riêng biệt)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# 4 hình có hai đầu tam giác (giống hình trong đề)
hinh = [
"""
      *
      * *
      * * *
* * * * * *  *    
* * *
* *  
*
""",
"""
      *
      * *
      *   *
* * * * * *  *    
*   *
* *  
*
""",
"""
       * * * *
       * * *
       * *
       *
     * * 
   * * *
 * * * *       
""",
"""
       * * * *
       *   *
       * *
       *
     * * 
   *   *
 * * * * 
"""
]

# In lần lượt 4 hình, mỗi hình xuất hiện sau 5 giây
for i in range(4):
    clear()
    print(f"Hình {i+1}:")
    print(hinh[i])
    time.sleep(5)

