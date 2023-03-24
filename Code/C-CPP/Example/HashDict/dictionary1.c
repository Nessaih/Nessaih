
/*
C语言实现字典：测试。
*/

#include <stdio.h>
#include <malloc.h>
#include <string.h>

struct nlist { /* table entry: */
    struct nlist *next; /* next entry in chain */
    char *name; /* defined name */
    char *defn; /* replacement text */
};

#define HASHSIZE 101
static struct nlist *hashtab[HASHSIZE]; /* pointer table */

/* hash: form hash value for string s */
unsigned hash(char *s)
{
    unsigned hashval;
    for (hashval = 0; *s != '\0'; s++)
        hashval = *s + 31 * hashval;
    return hashval % HASHSIZE;
}

/* lookup: look for s in hashtab */
struct nlist *lookup(char *s)
{
    struct nlist *np;
    for (np = hashtab[hash(s)]; np != NULL; np = np->next)
        if (strcmp(s, np->name) == 0)
            return np; /* found */
    return NULL; /* not found */
}
//避免使用strcpy函数VS报错：unsafe
#pragma warning(disable:4996)
char *strdup(char *s) /* make a duplicate of s */
{
    char *p;
    p = (char *)malloc(strlen(s) + 1); /* +1 for ’\0’ */
    if (p != NULL)
        strcpy(p, s);
    return p;
}

/* install: put (name, defn) in hashtab */
struct nlist *install(char *name, char *defn)
{
    struct nlist *np;
    unsigned hashval;
    if ((np = lookup(name)) == NULL) { /* not found */
        np = (struct nlist *) malloc(sizeof(*np));
        if (np == NULL || (np->name = strdup(name)) == NULL)
            return NULL;
        hashval = hash(name);
        np->next = hashtab[hashval];
        hashtab[hashval] = np;
    }
    else /* already there */
        free((void *)np->defn); /*free previous defn */
    if ((np->defn = strdup(defn)) == NULL)
        return NULL;
    return np;
}


/*"hx"，"bh","ep"散列值相同,*/
void test(void)
{
    struct nlist *p;
    p = install((char *)"hx", (char *)"48");
    p = p->next;
    p = install((char *)"bh", (char *)"56");
    p = p->next;
    p = install((char *)"swj", (char *)"22");
    p = p->next;
    p = install((char *)"tqy", (char *)"33");
    p = p->next;
    p = install((char *)"lqs", (char *)"14");
    p = p->next;
    p = install((char *)"ep", (char *)"21");
    p = p->next;
    p = NULL;

    p = lookup((char *)"ep");
    printf("%s\n", p->defn);
}

void test2(void)
{
    char x, y;
    printf("%d  %d %d\n", 'h', 'x', ('h'*31+'x')%101);

    for (x = 'a'; x <= 'z'; x++)
        for (y = 'a'; y <= 'z'; y++)
            if ((x * 31 + y) % 101 == 11)
                printf("%c%c\n", x, y);
}
int main(void)
{
    test();
    
    return 0;
}
