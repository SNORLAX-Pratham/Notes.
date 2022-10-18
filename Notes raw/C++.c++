#include <iostream> // Pre process command
#include <string>
using namespace std;
int main()
{
    cout << "Hello world"; // cout consol out(Print in console)
    return 0;
    int a, b, c;
    short a;
    long b;
    long long d;
    float no = 65.736; //! Increasing order of size
    double;
    long double;
    float const t = 76; // const is used to save constant

    // camelCase Notation
    int marksInMaths = 87;
    cout << marksInMaths;

    // User input
    int g;
    cout << " enter a number" << endl; // endl use for end line
    cin >> g;                          // Takes input from user (console in)

    // !Arithamatic operator
    int s = 2;
    int f = 7;
    cout << "s+f is" << s + f << endl;
    cout << "s-f is" << s - f << endl;
    cout << "s*f is" << s * f << endl;
    cout << "s/f is" << s / f << endl;

    //! And(&)  Or(||)   Not(!)

    // !If Else

    //*IF

    if (/* condition */)
    {
        /* code */
    }

    //*elseif

    else if (/* condition */)
    {
        /* code */
    }
    //* else

    else
        (/* condition */)
        {
            /* code */
        }

    //! Switch statements
    switch (expression)
    {
    case /* constant-expression */:
        /* code */
        break; // If you dont put break then it will execute all the code bellow

    default:
        break;
    }

    //! Loops
    //*While
    while (/* condition */)
    {
        /* code */
    }

    //*dowhile
    do
    {
        /* code */
    } while (/* condition */);

    //*for loop
    for (size_t i = 0; i < count; i++)
    {
        /* code */
    }

    //! Arrays: Collection of data
    int arr[2] = {
        1,
        2,
    };

    //! Strings
    string name = "Pratham";

    //! Pointers concept
    int a = 34;
    int *ptra; // the * star stores the data of the int in ptra

    ptra = &a; //& is used to laocate adress of the data

    //! object and classes
    class C
    {
    private:
        /* data */
    public:
        C(/* args */);
        ~C();
    };

    C::C(/* args */)
    {
    }

    C::~C()
    {
    }
}
//! Functions
int add(int l, int n)
{
    int y;
    y = l + n;
    return y;
}
