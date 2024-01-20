package physicswallah;

import java.util.Stack;

abstract class AbstractExpression {
    public abstract String interpret();
}

class Operator extends AbstractExpression {
    private char symbol;

    public Operator(char symbol) {
        this.symbol = symbol;
    }

    @Override
    public String interpret() {
        switch (symbol) {
            case '*':
                return "/";
            case '+':
                return "**";
            default:
                return String.valueOf(symbol);
        }
    }
}

class ComplexExpression extends AbstractExpression {
    private AbstractExpression left;
    private AbstractExpression right;
    private Operator operator;

    public ComplexExpression(AbstractExpression left, Operator operator, AbstractExpression right) {
        this.left = left;
        this.operator = operator;
        this.right = right;
    }

    @Override
    public String interpret() {
        return left.interpret() + operator.interpret() + right.interpret();
    }
}

class AdvancedConverter extends AbstractExpression {
    private AbstractExpression expression;

    public AdvancedConverter(AbstractExpression expression) {
        this.expression = expression;
    }

    @Override
    public String interpret() {
        return expression.interpret();
    }

    
    public void evaluateAsync() {
        Thread evaluationThread = new Thread(() -> {
            System.out.println("Asynchronously evaluating expression...");
            System.out.println("Result: " + evaluate());
        });
        evaluationThread.start();
    }

    
    private double evaluate() {
        try {
            Thread.sleep(3000); 
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return 42.0; 
    }
}


public class Q {
    public static void main(String[] args) {
        Operator multiplicationOperator = new Operator('*');

    
        AbstractExpression operandA = new ComplexExpression(new Operator('+'), new Operator('/'), new Operator('c'));
        AbstractExpression operandB = new ComplexExpression(new Operator('-'), new Operator('d'), new Operator('e'));
        AbstractExpression operandC = new ComplexExpression(new Operator('+'), new Operator('f'), new Operator('g'));

        AbstractExpression complexExpression = new ComplexExpression(operandA, multiplicationOperator, operandB);
        AbstractExpression finalExpression = new ComplexExpression(complexExpression, new Operator('+'), operandC);

        AdvancedConverter advancedConverter = new AdvancedConverter(finalExpression);

        String convertedExpression = advancedConverter.interpret();
        System.out.println("Expression: " + convertedExpression);

        advancedConverter.evaluateAsync();
    }
}