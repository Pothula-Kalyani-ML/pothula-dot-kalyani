def sum_even_num_odd_place(list_arg):
    sum=0
    for i in range(1,len(list_arg),2):
        if list_arg[i]%2==0:
            sum=sum+list_arg[i]
    return sum


if __name__ == "__main__":
    list1=[1, 2, 3, 4, 5, 6, 7]
    list2=[1, 2, 8, 3, 9, 4]
    list3=[2,3,4,5,6,7]
    result1=sum_even_num_odd_place(list1)
    result2=sum_even_num_odd_place(list2)
    result3=sum_even_num_odd_place(list3)
    print(f"list1{list1},sum of even number at odd places:{result1}")
    print(f"list2{list2},sum of even number at odd places:{result2}")
    print(f"list3{list3},sum of even number at odd places:{result3}")
