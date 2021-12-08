#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[]) {
    FILE *fp;
    fp = fopen("input02.txt", "r");
    
    char s[64];
    int r;

    int depth = 0;
    int distance = 0;

    while (!feof (fp)) { 
      fscanf (fp, "%s", &s);
      fscanf (fp, "%d", &r);

      if(strcmp(s, "up") == 0) {
        depth -= r;
      } else if(strcmp(s, "down") == 0) {
        depth += r;
      } else {
        distance += r;
      }
    }

    printf("%d\n", depth*distance);

    fclose (fp);
    return 0;
}
