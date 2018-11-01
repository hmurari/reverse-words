#include <stdio.h>
#include <string.h>

void swap(char *a, char *b) {
    char tmp;
    tmp = *a;
    *a = *b;
    *b = tmp;
}

void reverse(char *str, int start, int end) {
    int i;
    if (str == NULL || start >= end) {
        return;
    }
    for (i = start; i < start + (end - start)/2; i++) {
        swap(&str[i], &str[start + end - 1 - i]);
    }
}

void reverse_words(char *str) {
    int i, j = 0;
    int len = strlen(str);

    // reverse entire string.
    reverse(str, 0, len);

    for (i = 0; i < len; i++)
        if (str[i] == ' ') {
            // reverse back individual words
            reverse(str, j, i);
            while (str[i] == ' ')
                i++;
            j = i;
        }

        // reverse last word
        reverse(str, j, i);
}

int main() {
    char str[] = "you shall not pass!";
    reverse_words(str);
    printf("%s\n", str);
}
