from tkinter import Tk, StringVar, Message, Button, Frame, Entry, Label
import math

# frequency search function
def search(arr, UL, LL): # Linear search
      count = 0
      for x in range(LL, UL + 1, 1):
            for ele in arr:
                  if ele <= UL:
                        if x == ele:
                              count += 1
                  else: break
      return count
# End
# DOWNLOADED FROM INTERNET (QUICKSORT)
# https://www.geeksforgeeks.org/quick-sort/
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
    for j in range(low , high): 
        # If current element is smaller than or equal to pivot 
        if   arr[j] <= pivot: 
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
# 
def quickSort(arr,low,high): 
    if low < high: 
        # pi is partitioning index, arr[p] is now at right place 
        pi = partition(arr,low,high) 
        # Separately sort elements before partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)
#
def display(LL, UL, f, x, TCB1, TCB2, CF1, CF2, RF, r, k, i, fx, m, xm, fxm, md):
      # Print all the value
      h1 = '+-------------------------------+------------+------------+--------------------------+------------+------------+------------+-------------+-----------+------------------+\n'
      h2 = '|\tClass \t|  f \t |   x \t |\tTCB \t |  <CF \t |  >CF \t |  %RF \t |  fx  \t |  (x - ẍ)  |  f(x - ẍ)  |\n'
      h3 = '+-------------------------------+------------+------------+--------------------------+------------+------------+------------+-------------+-----------+------------------+\n'
      a = ''
      for ix in range(k):
            a += '| '+str(LL[ix])+' - '+str(UL[ix])+'\t\t| '+str(f[ix])+'\t| '+str('%g'%x[ix])+'\t| '+str(TCB1[ix])+' - '+str(TCB2[ix])+'\t| '+str(CF1[ix])+'\t| '+str(CF2[ix])+'\t| '+str('%.2g'%RF[ix])+'\t| '+str('%g'%fx[ix])+'\t| '+str('%.4g'%xm[ix])+'\t| '+str('%.4g'%fxm[ix])+'\t|\n'
      hn = '+-------------------------------+------------+------------+--------------------------+------------+------------+------------+-------------+-----------+------------------+'
      to = '\n|\t\t| '+str(sum(f))+'\t|\t|\t\t|\t|\t|\t| '+str('%.5g'%m)+'\t|\t| '+str('%.5g'%md)+'\t|'
      sv = '\n\nRange Value (RV=HV-LV):\t\t'+str(r)+'\nClass Interval (k=1+3.33log(n)):\t'+str(k)+'\nClass Size (i=RV/k):\t\t'+str(i)
      fdt.set(h1+h2+h3+a+hn+to+sv)
#
def main():
      new_data = ''
      input_data = inpt.get()
      if ',' in input_data:
            new_data = input_data.split(',')
      elif ' ' in input_data:
            new_data = input_data.split()
      # SAVE THE DATA IN ARRAY
      array = []
      try:
            for element in new_data:
                  array.append(int(element))
            n = len(array)
            # SORT THE DATA
            quickSort(array, 0, n-1)
            # get the lowest Value(LV) and High Value(HV) from the array
            LV = array[0]; HV = array[n-1]
            # ==========COMPUTATION===========
            # Compute for the RANGE (r)
            r = HV - LV
            # Compute for the class interval (k)
            k = round(1 + 3.33*math.log10(n))
            # Compute for the class size (i)
            i = round(r/k)
            # ============END=================
            # Get the LL and the UL
            arr_LL = []; arr_UL = []
            arr_LL.append(LV)
            UL = LV + i - 1
            arr_UL.append(UL)
            for b in range(k - 1):
                  LL = UL + 1
                  arr_LL.append(LL)
                  UL = LL + i - 1
                  arr_UL.append(UL)
            # Get the frequency of data (f)
            f = []
            for c in range(k):
                  fcount = search(array, arr_UL[c], arr_LL[c])
                  f.append(fcount)
            # class mark (x) average of ((LL + UL)/2), then x += i
            x = []
            cmark = float((arr_UL[0] + arr_LL[0])/2)
            x.append(cmark)
            for d in range(k-1):
                  cmark += i
                  x.append(cmark)
            # MEAN fx
            fx = []
            for d2 in range(k):
                  fxh = f[d2]*x[d2]
                  fx.append(round(fxh, 4))
            mean = sum(fx)/n
            # (x - ẍ)
            xm = []
            for d3 in range(k):
                  mnx = abs(x[d3] - mean)
                  xm.append(mnx)
            # f(x - ẍ)
            fxm = []
            for d4 in range(k):
                  fmnx = f[d4] * xm[d4]
                  fxm.append(fmnx)
            mad = sum(fxm)/n
            # TCB -0.5 +0.5
            TCB1 = []; TCB2 = []
            for e in arr_LL:
                  tcb1 = e - 0.5
                  TCB1.append(tcb1)
            for j in arr_UL:
                  tcb2 = j + 0.5
                  TCB2.append(tcb2)
            # <CF=CF+f; CF=n, >CF=CF-f
            CF1 = []; CF2 = []
            cf1 = f[0]
            CF1.append(cf1)
            cf2 = n
            CF2.append(cf2)
            for g in range(1, k, 1):
                  cf1 += f[g]
                  CF1.append(cf1)
            for h in range(k):
                  cf2 -= f[h]
                  CF2.append(cf2)
            # Relative Frequency (RF) = f/n*100
            RF = []
            for l in f:
                  rf = l/n*100
                  RF.append(rf)
            # display the table, sorted array and stem leaf
            display(arr_LL, arr_UL, f, x, TCB1, TCB2, CF1, CF2, RF, r, k, i, fx, mean, xm, fxm, mad)
            # plotline(f, x)
            # plotpie(RF)
            # plotbar(f, TCB1, TCB2)
      except:
            fdt.set('Invalid data set!\n' + input_data)
      
parent = Tk()
parent.title("Frequency Distributon Table PYTHON TKINTER")
#win.iconbitmap("czero.ico")
parent.resizable(0,0)
# WIDGET
fdt = StringVar()
inpt = StringVar()
window = Frame(parent).pack()
title = Message(window, font = ('arial', 13),
            text = 'FREQUENCY DISTRIBUTION TABLE\n\tCreated by: Bishop', width = 600).pack(pady = 5)
lbl = Label(window, font = ('arial', 11),
            text = 'Input the Data here [separated by space or a comma]:').pack(anchor = 'w', padx = 5)
inp = Entry(window, font = ('arial', 15, 'bold'),
            fg = 'black', bg = 'lightgray', width = 70, textvariable = inpt).pack(pady = 4, padx = 5, anchor = 'w')
button = Button(window, font = ('arial', 10),
            bg = 'blue', bd = 5, text = 'Compute', command = lambda : main()).pack(anchor = 'w', padx = 5)
fdttable = Label(window, font = ('arial', 10),
            fg = 'black', bg = 'lightgray', width = 97, height = 35, textvariable = fdt, anchor = 'n').pack(pady = 4)
# MASTER/PARENT WINDOW SIZE
parent.minsize(width = 800, height = 600)
parent.mainloop()
