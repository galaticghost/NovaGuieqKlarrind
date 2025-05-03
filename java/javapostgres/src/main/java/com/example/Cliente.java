package com.example;

public class Cliente {
    private String nome;
    private Double salario;
    private int idade;
    private int id;

    public Cliente(String nome, int idade, Double salario){
        this.nome = nome;
        this.salario = salario;
        this.idade = idade;
    }

    public Cliente(String nome, int idade, Double salario, int id){
        this(nome, idade, salario);
        this.id = id;
    }
}
