#include <ctype.h>
#include <stdarg.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>

#define nullptr NULL

typedef enum
{
    TK_sign,
    TK_num,
    TK_EOL,
} TokenKind;

typedef struct Token Token;

struct Token
{
    TokenKind kind;
    Token *nex;
    long num;
    char *str;
};

Token *now_token;

bool TK_isSign(char oper) // Token
{
    if (now_token->kind != TK_sign || now_token->str[0] != oper)
        return false;
    return true;
}

long TK_takeInt() // Token
{
    if (now_token->kind != TK_num)
    {
        printf("ERROR\n");
        exit(1);
    }
    return now_token->num;
}

bool isEOL() { return (now_token->kind == TK_EOL); } // Token

Token *new_Token(TokenKind TKK, char *str)
{
    Token *tmp = calloc(1, sizeof(Token));
    tmp->kind = TKK;
    tmp->str = str;
    tmp->nex = nullptr;
    return tmp;
}

bool isSign(char ch)
{
    if (ch == '+' || ch == '-' || ch == '*' || ch == '/')
        return true;
    return false;
}

Token *tokenize(char *s)
{
    Token head; // head is a EMPTY token, and shouldn't be returned
    head.nex = nullptr;
    Token *tail = &head;

    while(*s)
    {
        if (isspace(*s))
        {
            ++s;
            continue;
        }

        if (isSign(*s))
        {
            tail->nex = new_Token(TK_sign, s++);
            tail = tail->nex;
            continue;
        }

        if (isdigit(*s))
        {
            tail->nex = new_Token(TK_num, s);
            tail->num = strtol(s, &s, 10);
            tail = tail->nex;
            continue;
        }

        printf("tokenize ERROR");
        exit(1);
    }

    tail->nex = new_Token(TK_EOL, s);
    tail = tail->nex;

    return head.nex;
}


int main()
{
    char *s;

    scanf("%s", s);

    now_token = tokenize(s);

    while(now_token->kind != TK_EOL)
    {

        now_token = now_token->nex;
    }

    return 0;
}
