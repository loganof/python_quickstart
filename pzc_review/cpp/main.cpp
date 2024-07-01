// NOTE: you need to compile the program with C++11 due to the use of lambda functions.
// Refer to README for detailed instructions.

#include <functional>
#include <iostream>

template <class T>
struct LinkedList {
    T head;
    LinkedList<T>* tail;
};


// For simplicity, proper memory management is not done: all heap-allocated memory are not properly released.
template <typename T>
LinkedList<T>* cons(T head, LinkedList<T>* tail = nullptr)
{
    return new LinkedList<T>{ head, tail };
}

template <typename T>
std::string listToString(LinkedList<T>* list)
{
    if (!list) {
        return "";
    }
    if (!list->tail) {
        return std::to_string(list->head);
    }
    return std::to_string(list->head) + " " + listToString(list->tail);
}

template <typename T1, typename T2>
LinkedList<T2>* myMap(std::function<T2(T1)> fn, LinkedList<T1>* list)
{
    if (!list) {
        return nullptr;
    }
    T2 head_value = fn(list->head);
    LinkedList<T2>* tail_value = myMap(fn, list->tail);
    return cons(head_value, tail_value);
}

template <typename T1, typename T2>
T2 myReduce(std::function<T2(T2, T1)> fn, T2 accm, LinkedList<T1>* list)
{
    if (!list) {
        return accm;
    }
    return myReduce(fn, fn(accm, list->head), list->tail);
}

template <typename T1, typename T2>
T2 myReduceRight(std::function<T2(T1, T2)> fn, T2 accm, LinkedList<T1>* list)
{
    // [BEGIN] YOUR CODE HERE
    // if list is empty, return accm
    if(!list){
        return accm;
    }
    // when traversing to the last node, calculate fn(list->head, accm) for the first time, then back to the last layer and caculate repeatedly.
    if(!list->tail)
        return fn(list->head, accm);
    // [END] YOUR CODE HERE
    return fn(list->head, myReduceRight(fn, accm, list->tail));
}


template <typename T1, typename T2>
LinkedList<T2>* myMap2(std::function<T2(T1)> fn, LinkedList<T1>* list)
{
    // [BEGIN] YOUR CODE HERE
    if (!list) return nullptr;

    std::function<LinkedList<T2> *(T1, LinkedList<T2> *)> cpFn = [&](T1 cur, LinkedList<T2> *acc) -> LinkedList<T2> *
    {
        auto newList = cons<T2>(0);
        newList->tail = acc;
        newList->head = cur;
        return newList;
    };
    
    LinkedList<T2> *ptr = nullptr;
    // 使用myReduceRight函数来递归地应用cpFn到整个链表
    decltype(auto) storeList = myReduceRight(cpFn, ptr, list);

    // 定义一个辅助函数来存储结果
    std::function<LinkedList<T2>*(LinkedList<T2>*)> storeFn = [&](LinkedList<T2>* store) -> LinkedList<T2>* {
        if (store == nullptr) {
            return nullptr;
        }
        store->head = fn(store->head);
        store->tail = storeFn(store->tail);
        return store;
    };

    // 应用storeFn到整个链表来存储结果
    return storeFn(storeList);
}


int main()
{
    LinkedList<int>* exampleList = cons(1, cons(2, cons(3, cons(4))));
    std::function<int(int)> plusOne = [](int x) { return x + 1; };
    std::function<int(int, int)> xTimesTwoPlusY = [](int x, int y) { return x * 2 + y; };
    std::function<int(int, int)> printXAndReturnY = [](int x, int y) { std::cout << x << std::endl; return y; };
    std::function<std::string(int)> toString = [](int x) { return std::to_string(x); };
    std::function<std::string(std::string, std::string)> unfoldCalculation = [](std::string x, std::string y) { return "fn(" + x + ", " + y + ")"; };
    std::function<int(int)> printAndReturn = [](int x) { std::cout << x << std::endl; return x; };
    std::cout << listToString(exampleList) << " should be 1 2 3 4" << std::endl;
    std::cout << listToString(myMap(plusOne, exampleList)) << " should be 2 3 4 5" << std::endl;
    std::cout << myReduce(xTimesTwoPlusY, 0, exampleList) << " should be 26" << std::endl;
    std::cout << myReduce(unfoldCalculation, std::string("accm"), myMap(toString, exampleList)) << " should be fn(fn(fn(fn(accm, 1), 2), 3), 4)" << std::endl;
    std::cout << myReduceRight(xTimesTwoPlusY, 0, exampleList) << " should be 20" << std::endl;
    std::cout << myReduceRight(unfoldCalculation, std::string("accm"), myMap(toString, exampleList)) << " should be fn(1, fn(2, fn(3, fn(4, accm))))" << std::endl;
    std::cout << "Below should output 4 3 2 1 each on a separate line:" << std::endl;
    myReduceRight(printXAndReturnY, 0, exampleList);
    std::cout << listToString(myMap2(plusOne, exampleList)) << " should be 2 3 4 5" << std::endl;
    std::cout << "The two outputs below should be equal:" << std::endl;
    std::cout << "First output:" << std::endl;
    myMap(printAndReturn, exampleList);
    std::cout << "Second output:" << std::endl;
    myMap2(printAndReturn, exampleList);
}
