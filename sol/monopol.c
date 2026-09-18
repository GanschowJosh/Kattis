#include <stdio.h>

int main() {
  int buckets[13];
  for(int i = 0; i <= 12; i++) {
    buckets[i]=0;
  }
  
  int sum;
  for(int i = 1; i <= 6; ++i) {
    for(int j = 1; j <= 6; ++j) {
      sum = i+j;
      buckets[sum]++;
    }
  }

  int N;
  scanf("%d", &N);

  int curr_hotel;
  float su = 0.0;
  for(int i = 0; i < N; i++) {
    scanf("%d", &curr_hotel);
    su+=buckets[curr_hotel];
  }
  
  printf("%f", su/36);

  for(int i = 1; i <= 12; ++i) {
    printf("Bucket %d: %d\n", i, buckets[i]);
  }
}