#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#include <stack>
#pragma warning(disable:4996)

using namespace std;

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
    Token* nex;
    int64_t num;
    char* str;
};

Token* now_token;

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
        printf("take Int ERROR\n");
        exit(1);
    }
    return now_token->num;
}

bool isEOL() { return (now_token->kind == TK_EOL); } // Token

Token* new_Token(TokenKind TKK, char* str)
{
    Token* tmp = (Token *)calloc(1, sizeof(Token));
    tmp->kind = TKK;
    tmp->str = str;
    tmp->nex = nullptr;
    return tmp;
}

bool isSign(char ch)
{
    if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '(' || ch == ')')
        return true;
    return false;
}

Token* tokenize(char* s)
{
    Token head; // head is a EMPTY token, and shouldn't be returned
    head.nex = nullptr;
    Token* tail = &head;

    while (*s)
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
            tail = tail->nex;
            tail->num = strtol(s, &s, 10);
            continue;
        }

        printf("tokenize ERROR");
        exit(1);
    }

    tail->nex = new_Token(TK_EOL, s);
    tail = tail->nex;

    return head.nex;
}

typedef enum
{
    NK_add,
    NK_sub,
    NK_mul,
    NK_div,
    NK_num
}NodeKind;

typedef struct node node;

struct node
{
    NodeKind kind;
    node *l, *r;
    int64_t val;
};

node* new_node(NodeKind NKK, node* l, node* r)
{
    node* p = (node *)calloc(1, sizeof(node));
    p->kind = NKK;
    p->l = l;
    p->r = r;
    return p;
}

node* new_node(NodeKind NKK, int64_t n)
{
    node* p = (node*)calloc(1, sizeof(node));
    p->kind = NKK;
    p->val = n;
    return p;
}

node* expr();
node* mul();
node* term();

node* expr()
{
    node* Node = mul();

    while (true)
    {
        if (TK_isSign('+'))
        {
            now_token = now_token->nex;
            Node = new_node(NK_add, Node, mul());
        }
        else if (TK_isSign('-'))
        {
            now_token = now_token->nex;
            Node = new_node(NK_sub, Node, mul());
        }
        else 
            return Node;

    }
}

node* mul()
{
    node* Node = term();

    while (true)
    {
        if (TK_isSign('*'))
        {
            now_token = now_token->nex;
            Node = new_node(NK_mul, Node, term());
        }
        else if (TK_isSign('/'))
        {
            now_token = now_token->nex;
            Node = new_node(NK_div, Node, term());
        }
        else
            return Node;
    }
}

node* term()
{
    node* Node = nullptr;
    if (TK_isSign('('))
    {
        now_token = now_token->nex;
        Node = expr();
        if (!TK_isSign(')'))
        {
            printf("term ERROR");
            exit(1);
        }
        now_token = now_token->nex;
        return Node;
    }

    Node = new_node(NK_num, TK_takeInt());
    now_token = now_token->nex;
    return Node;
}

stack<int64_t> st;

void cal(node* p)
{
    if (p->kind == NK_num)
    {
        st.push(p->val);
        return;
    }

    cal(p->l); cal(p->r);

    long b = st.top(); st.pop();
    long a = st.top(); st.pop();

    switch (p->kind)
    {
    case NK_add:
        st.push(a + b);
        return;

    case NK_sub:
        st.push(a - b);
        return;

    case NK_mul:
        st.push(a * b);
        return;

    case NK_div:
        st.push(a / b);
        return;

    default:
        break;
    }

    return;
}

int main()
{
    int n;
    scanf("%d", &n);

    while (n--)
    {
        char s[1000];

        scanf("%s", s);

        now_token = tokenize(s);

        node* ex = expr();

        cal(ex);

        printf("%lld\n", st.top());

        st = stack<int64_t>();
    }
    return 0;
}
