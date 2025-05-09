package com.example;

public class Cliente {
    private String nome;
    private Double salario;
    private int idade;
    private int id;

    public Cliente(String nome, int idade, Double salario) {
        this.nome = nome;
        this.idade = idade;
        this.salario = salario;
    }

    public Cliente(String nome, int idade, Double salario, int id) {
        this(nome, idade, salario);
        this.id = id;
    }

    @Override
    public String toString() {
        if (this.id == 0) {
            return String.format("Nome: %s, Idade: %d, Salario: R$%.2f", this.nome, this.idade,
                    this.salario);
        } else {
            return String.format("Id: %d, Nome: %s, Idade: %d, Salario: R$%.2f", this.id, this.nome, this.idade,
                    this.salario);
        }
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Double getSalario() {
        return salario;
    }

    public void setSalario(Double salario) {
        this.salario = salario;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
}
