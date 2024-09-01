# Tutorial

The purpose of this document is to help you get started on solving the
challenges.

If you're used to competitive programming, you don't need to read this
tutorial as you probably won't learn anything new.

## Input/Output

Unless specifically stated in the challenge description, your program should
always read from `stdin` and write to `stdout`. How to do that depends on the
language you are using.

Here are some examples.

### I/O with Python

```python
from sys import stdin, stdout


for line in stdin:
    # Do someting with data, then output the result.
    stdout.write(answer)
```

### I/O with C++

```cpp
#include <iostream>
#include <string>

using namespace std;

int main(void)
{
    string line;

    while (getline(cin, line)) {
        // Solve test case, then output the result.
        cout << answer << endl;
    }

    return 0;
}
```

### I/O with NodeJS

```js
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', (line) => {
  // Do something with the data and output the result.
  console.log(answer);
});
```

### I/O with Java

```java
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Scanner can be really slow on large inputs.
        // Use a buffered reader when dealing with large inputs.
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();

            // Solve the test case and output its answer.
            System.out.println(answer);
        }
    }
}
```

## How to run your programs

Once you are done writting your solution, you can compile it and then run it
on test data with I/O redirections.

### Python

```bash
python program.py < in.txt > out.txt
```

### C++

```bash
g++ -o program -std=c++17 main.cpp
./program < input.txt > output.txt
```

### NodeJS

```bash
node program.js < input.txt > output.txt
```

### Java

```bash
javac MyProgram.java
java MyProgram
````
