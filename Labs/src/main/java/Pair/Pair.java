package Pair;

public class Pair<T, T1> {
    private T first;
    private T1 second;

    public Pair(T t, T1 t1){
        this.first = t;
        this.second = t1;
    }

    public T getFirst()
    {
        return this.first;
    }
    public T1 getSecond(){
        return this.second;
    }

}
