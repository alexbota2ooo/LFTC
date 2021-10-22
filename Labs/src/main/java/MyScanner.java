import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class MyScanner {

    SymbolTable symbolTable;
    LanguageSpecification specification = new LanguageSpecification();
    private String filePath;

    public MyScanner(String filePath){
        this.filePath = filePath;
        this.symbolTable = new SymbolTable(100);
    }

    private String readFile() throws FileNotFoundException{
        StringBuilder fileContent = new StringBuilder();
        java.util.Scanner scanner = new java.util.Scanner(new File(this.filePath));
        while (scanner.hasNextLine()) {
            fileContent.append(scanner.nextLine());
        }
        return fileContent.toString()
                .replace("\n", "").replace("\t", "");
    }
    public List<String> tokenize() {
        try {
            String fileContent = this.readFile();
            return new ArrayList<>(List.of(fileContent.split("[{};: ,\\[\\]()\"]")))
                    .stream()
                    .filter(possibleToken -> possibleToken.length() > 0)
                    .collect(Collectors.toList());
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        return null;
    }



    public boolean isSeparator(String ch){
        return specification.getSeparators().contains(ch);
    }

    public boolean isOperator(String ch){
        return specification.getOperators().contains(ch);
    }

    public boolean isReservedWord(String ch){
        return specification.getReservedWords().contains(ch);
    }

    public boolean isConstant(String ch){
        return (isCharacter(ch) || isInteger(ch));
    }

    public boolean isCharacter(String ch){
        Pattern pattern = Pattern.compile("^'[a-zA-Z0-9]'$");
        return (pattern.matcher(ch).matches());
    }

    public boolean isInteger(String ch){
        Pattern pattern = Pattern.compile("[-]?\\d+");
        return (pattern.matcher(ch).matches());
    }

}