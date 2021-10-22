public class main {

    public static void main(String[] args){
        SymbolTable st = new SymbolTable(100);

        /*System.out.println(st.Add("a"));
        System.out.println(st.Add("b"));
        System.out.println(st.Add("d"));
        System.out.println(st.Add("d"));
        System.out.println(st.Add("l"));
        System.out.println(st.Add("ab"));
        System.out.println(st.Add("ba"));

        System.out.println(st.Search("a"));
        System.out.println(st.Search("b"));
        System.out.println(st.Search("d"));
        System.out.println(st.Search("l"));
        System.out.println(st.Search("ab"));
        System.out.println(st.Search("ba"));*/
        LanguageSpecification languageSpecification = new LanguageSpecification();
        System.out.println(languageSpecification);
        MyScanner scanner = new MyScanner("F:\\FLCD\\Labs\\src\\main\\java\\p2.txt");
        System.out.println(scanner.tokenize());
    }
}