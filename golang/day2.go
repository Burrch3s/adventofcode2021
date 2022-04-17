// Day2 solution in golang
package main


import (
    "fmt"
    "os"
)


// Submarine struct to help conceptialize the problem
type Submarine struct {
    X, Depth, Aim int
}

// Forward - moves the Submarine forward by the num amount
func (sub *Submarine) Forward(num int) {
    //fmt.Println("sub moved forward", num)
    sub.X += num
    sub.Depth += sub.Aim * num
}

// Up - moves the sub up by the num amount
func (sub *Submarine) Up(num int) {
    //fmt.Println("sub moved up", num)
    //sub.Depth -= num
    sub.Aim -= num
}

// Down - moves the sub down by the num amount
func (sub *Submarine) Down(num int) {
    //fmt.Println("sub moved down", num)
    //sub.Depth += num
    sub.Aim += num
}


// partOne - Ends up driving solution for both parts, the difference in logic
// between part one and two are in the Submarine methods. Part 1 is commented out,
// and part 2 is currently implemented which tweaks Aim to drive the sub
func partOne() (answer int, err error) {
    sub := Submarine{X: 0, Depth: 0, Aim: 0}

    // Iterate over day2.input and move sub accordingly
    b, err := os.Open("./day2.input")
    if err != nil { return -1, err }

    for {
        var method string
        var number int

        n, err := fmt.Fscanln(b, &method, &number)
        if n == 0 || err != nil {
            break
        }

        switch method {
        case "forward":
            sub.Forward(number)
        case "up":
            sub.Up(number)
        case "down":
            sub.Down(number)
        default:
            panic(fmt.Sprintln("Error occurred reading method:", method))
        }
    }
    fmt.Println("sub positions", sub.X, sub.Depth, sub.Aim)
    return sub.X * sub.Depth, nil
}

func main() {
    answer, err := partOne()
    if err != nil {
        fmt.Println("Error occurred:", err)
        return
    }

    fmt.Println("answer:", answer)
}
