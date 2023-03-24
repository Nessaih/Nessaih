
/*
C语言实现字典：测试。
*/

#include <stdio.h>
#include <malloc.h>
#include <string.h>

struct nlist { /* table entry: */
	struct nlist *next; /* next entry in chain */
	char *name; /* defined name */
	unsigned int value; /* replacement text */
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

/* install: put (name, value) in hashtab */
struct nlist *install(char *name, unsigned int value)
{
	struct nlist *np;
	unsigned hashval;
	if ((np = lookup(name)) == NULL) { /* not found */
		np = (struct nlist *)malloc(sizeof(*np));
		if (np == NULL || (np->name = strdup(name)) == NULL)
			return NULL;
		hashval = hash(name);
		np->next = hashtab[hashval];
		hashtab[hashval] = np;
	}
	np->value = value;
	return np;
}


/*"hx"，"bh","ep"散列值相同,*/
void test(void)
{
	struct nlist *p;
	p = install((char *)"hx", 48);
	p = p->next;
	p = install((char *)"bh", 56);
	p = p->next;
	p = install((char *)"swj", 22);
	p = p->next;
	p = install((char *)"tqy", 33);
	p = p->next;
	p = install((char *)"lqs", 14);
	p = p->next;
	p = install((char *)"ep", 21);
	p = p->next;
	p = NULL;

	p = lookup((char *)"swj");
	if (NULL != p)
		printf("%d\n", p->value);
	else
		printf("not found\n");
}


int main(void)
{
	test();
	
	return 0;
}
