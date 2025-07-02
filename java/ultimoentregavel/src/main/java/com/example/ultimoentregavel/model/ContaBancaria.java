package com.example.ultimoentregavel.model;

import jakarta.persistence.Id;
import jakarta.persistence.Table;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;

@Entity
@Table(name = "conta_bancaria")
public class ContaBancaria {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column(unique = true)
    private String numeroConta;
    private String nomeTitular;
    private Double saldo;
    private boolean ativo;

    public ContaBancaria() {

    }

    public ContaBancaria(String numeroConta, String nomeTitular, boolean ativo) {
        this.numeroConta = numeroConta;
        this.nomeTitular = nomeTitular;
        this.ativo = ativo;
        this.saldo = 0.00;
    }

    public boolean depositar(Double valor) {
        if (valor < 0) {
            return false;
        } else {
            this.saldo = this.saldo + valor;
            return true;
        }
    }

    public boolean sacar(Double valor) {
        if (valor < 0 || valor > this.saldo) {
            return false;
        } else {
            this.saldo = this.saldo - valor;
            return true;
        }
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNumeroConta() {
        return numeroConta;
    }

    public void setNumeroConta(String numeroConta) {
        this.numeroConta = numeroConta;
    }

    public String getNomeTitular() {
        return nomeTitular;
    }

    public void setNomeTitular(String nomeTitular) {
        this.nomeTitular = nomeTitular;
    }

    public Double getSaldo() {
        return saldo;
    }

    public void setSaldo(Double saldo) {
        this.saldo = saldo;
    }

    public boolean isAtivo() {
        return ativo;
    }

    public void setAtivo(boolean ativo) {
        this.ativo = ativo;
    }

    public void criarConta(ContaBancaria conta) {

    }

}
