import Pair.Pair;

import java.io.*;
import java.util.*;
import java.util.regex.Pattern;
import java.util.stream.Collectors;




public class MyScanner {

    SymbolTable symbolTable;
    LanguageSpecification specification = new LanguageSpecification();
    private String filePath;
    private ProgramInternalForm pif;
    public MyScanner(String filePath){
        this.filePath = filePath;
        this.symbolTable = new SymbolTable(100);
        this.pif = new ProgramInternalForm();
    }

    /*private String readFile() throws FileNotFoundException{
        StringBuilder fileContent = new StringBuilder();
        java.util.Scanner scanner = new java.util.Scanner(new File(this.filePath));
        while (scanner.hasNextLine()) {
            fileContent.append(scanner.nextLine());
        }
        return fileContent.toString()
                .replace("\n", "").replace("\t", "");
    }
    */

    public void ScanFile() {
        try {
            File file = new File(this.filePath);
            BufferedReader br = new BufferedReader(new FileReader(file));
            int i = 0;
            String line;
            StringBuilder output = new StringBuilder();

            while((line = br.readLine()) != null) {
                List<String> tokenList = TokenizeLine(line);
                System.out.println(tokenList);
                ScanLine(tokenList, i, output);
                i++;
            }

            WritePifToFile(output);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void WritePifToFile(StringBuilder output) {
        try {
            String filename = "F:\\FLCD\\Labs\\src\\main\\java\\Output.txt";
            FileWriter fw = new FileWriter(filename);
            fw.write(symbolTable.toString());
//            fw.write(pif.toString());
            fw.write(output.toString());
            fw.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void ScanLine(List<String> tokens, int line, StringBuilder output) {
        String lastToken = "";

        for(int i = 0; i < tokens.size(); ++i) {
            String token = tokens.get(i);

            if (isConstant(token)){
                int code = specification.getCodification().get("constant"); // 1
                symbolTable.Add(token);
                var position = symbolTable.Search(token);
                pif.Add(code, position);
                output.append("Token " + token + " -> pos: " + position + "\n");
            }
            else if ((token.equals("-") || token.equals("+")) && (isNumber(tokens.get(i + 1))) &&
                    (lastToken.equals("=") || lastToken.equals("("))) {
                token += tokens.get(i + 1);
                i++;
                if (!token.equals("-0")){
                    int code = specification.getCodification().get("constant"); // 1
                    symbolTable.Add(token);
                    var position = symbolTable.Search(token);
                    pif.Add(code, position);
                    output.append("Token " + token + " -> pos: " + position + "\n");
                }
                else {
                    output.append("Error at line " + line + ". Invalid token: " + token + "\n");
                }
            }
            else if (isOperator(token) || isSeparator(token) || isReservedWord(token)) {
                int code = specification.getCodification().get(token);
                pif.Add(code, -1);
                output.append("Token " + token + " -> pos: " + -1 + "\n");
            }
            else if (isIdentifier(token)){
                int code = specification.getCodification().get("identifier"); // 0
                symbolTable.Add(token);
                var position = symbolTable.Search(token);
                pif.Add(code, position);
                output.append("Token " + token + " -> pos: " + position + "\n");
            }
            else {
                output.append("Error at line " + line + ". Invalid token: " + token + "\n");
            }
            lastToken = token;
        }
    }



    public List<String> TokenizeLine(String line) {
        List<String> tokens = new ArrayList<>();
        int i = 0;

        while (i < line.length()) {

            if (line.charAt(i) == '"') {
                // user declared strings
                StringBuilder stringToken = new StringBuilder("\"");
                i++;
                while (i < line.length() && line.charAt(i) != '"') {
                    stringToken.append(line.charAt(i));
                    i++;
                }
                stringToken.append("\"");
                i++;
                tokens.add(stringToken.toString());
            }
            else if (isSeparator(String.valueOf(line.charAt(i)))) {
                // separators excluding space, tab and new line
                if (!(line.charAt(i) == ' ') && !(line.charAt(i) == '\t') && !(line.charAt(i) == '\n')) {
                    tokens.add(String.valueOf(line.charAt(i)));
                }
                i++;
            }
            else if (isOperator(String.valueOf(line.charAt(i)))) {
                // composed operators and operators
                if(isOperator(String.valueOf(line.charAt(i + 1)))) {
                    tokens.add(line.charAt(i) + String.valueOf(line.charAt(i + 1)));
                    i = i + 2;
                }
                else {
                    tokens.add(String.valueOf(line.charAt(i)));
                    i++;
                }
            }
            else {
                //reserved words, constants and identifiers
                StringBuilder token = new StringBuilder(String.valueOf(line.charAt(i)));
                i++;
                while (i < line.length() && !isSeparator(String.valueOf(line.charAt(i))) && !isOperator(String.valueOf(line.charAt(i)))) {
                    token.append(line.charAt(i));
                    i++;
                }
                tokens.add(token.toString());
            }
        }

        return tokens;
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
        Pattern pattern = Pattern.compile("^'[a-zA-Z0-9]'$"); // any character
        return (pattern.matcher(ch).matches());
    }

    public boolean isInteger(String ch){
        Pattern pattern = Pattern.compile("[-]?\\d+");  // simple int
        return (pattern.matcher(ch).matches());
    }

    public boolean isNumber(String token){
        String number = "^([+|-]?[1-9][0-9]*)|0$";  //zero or one of [+ or -] [1-9] , 0 or more [0-9]
        return token.matches(number);
    }

    public boolean isIdentifier(String token){
        String pattern = "^[a-zA-Z]([a-zA-Z0-9_]*$)"; //(..) 0 or more occurrences
        return token.matches(pattern);
    }
}