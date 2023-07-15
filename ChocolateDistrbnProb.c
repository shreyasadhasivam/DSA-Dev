#include<stdio.h>
#include<stdlib.h>
#define INT_MAX 99999;

int cmpfunc(const void*a , const void*b){
    return (*(int*)a -*(int*)b);
}

int minimumDiff(int*arr, int n, int m){
    if(m==0 || n==0)
        return 0;
    qsort(arr, n, sizeof(int), cmpfunc);
    printf("\nThe sorted array is:");
    for(int j=0;j<n;j++){
        printf("%d ", arr[j]);
    }

    if(n<m)
        return -1;

    int minDiff = INT_MAX;
    for(int i=0;i<n-m;i++){
        if(arr[i+m-1]-arr[i]<minDiff){
            minDiff =arr[i+m-1]-arr[i];
        }
    }
    return minDiff;
}

int main(){
    int n,m;
    printf("Enter the number of elements:\n");
    scanf("%d",&n);
    int arr[100];
    printf("\nEnter the elements:\n");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("\nThe array is:");
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
    printf("\nEnter the number of students:");
    scanf("%d", &m);
    printf("\nMinimum difference is: %d", minimumDiff(arr,n, m));
    return 0;
}