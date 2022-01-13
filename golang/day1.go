package main

import (
    "fmt"
    "strconv"
    "strings"
    "io/ioutil"
)

/*
taken from SO. reading in lines and converting to nums, storing in a array
*/
func readFile(fname string) (nums []int, err error) {
    b, err := ioutil.ReadFile(fname)
    if err != nil { return nil, err }

    lines := strings.Split(string(b), "\n")

    // Assign cap to avoid resize on every append.
    nums = make([]int, 0, len(lines))

    for _, l := range lines {
        // Empty line occurs at the end of the file when we use Split.
        if len(l) == 0 { continue }
        // Atoi better suits the job when we know exactly what we're dealing
        // with. Scanf is the more general option.
        n, err := strconv.Atoi(l)
        if err != nil { return nil, err }
        nums = append(nums, n)
    }

    return nums, nil
}

func day1() (answer int) {
    nums, err := readFile("day1.input")
    if err != nil { panic(err) }

    ret := 0

    for index, num := range nums {
        prev := index - 1
        if prev < 0 { continue }

        if nums[prev] < num {
            ret = ret + 1
        }
    }

    return ret
}

func day2() (answer int) {
    nums, err := readFile("day1.input")
    if err != nil { panic(err) }

    ret := 0
    total := len(nums)

    for index := range nums {
        prev := index - 1
        if prev < 0 { continue }
        if index == total - 2 { break }  // break when not enough nums for 3-window-sum

        prevSum := nums[prev] + nums[index] + nums[index+1]
        currSum := nums[index] + nums[index+1] + nums[index+2]


        if prevSum < currSum {
            ret = ret + 1
        }
    }

    return ret
}

func main() {
    answer := day1()
    fmt.Println(answer)
    answer = day2()
    fmt.Println(answer)
}
