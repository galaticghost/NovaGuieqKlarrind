package com.example.ultimoentregavel.service;

import java.util.List;

import org.springframework.stereotype.Service;

import com.example.ultimoentregavel.model.ContaBancaria;
import com.example.ultimoentregavel.repository.ContaBancariaRepository;

@Service
public class ContaBancariaService {
    private final ContaBancariaRepository contaBancariaRepository;

    public ContaBancariaService(ContaBancariaRepository contaBancariaRepository) {
        this.contaBancariaRepository = contaBancariaRepository;
    }

    public ContaBancaria criarConta(ContaBancaria contaBancaria) {
        return contaBancariaRepository.save(contaBancaria);
    }

    public List<ContaBancaria> buscarTodasContas() {
        return contaBancariaRepository.findAll();
    }

    public ContaBancaria buscarContaPorId(Long id) {
        return contaBancariaRepository.findById(id).orElseThrow();
    }

    public ContaBancaria depositar(Long id, Double valor) {
        ContaBancaria conta = contaBancariaRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Não foi encontrada uma conta com o id " + id + "."));
        boolean atualizou = conta.depositar(valor);
        if (atualizou == true) {
            return contaBancariaRepository.save(conta);
        } else {
            throw new RuntimeException("O valor enviado é inválido");
        }
    }

    public ContaBancaria sacar(Long id, Double valor) {
        ContaBancaria conta = contaBancariaRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Não foi encontrada uma conta com o id " + id + "."));
        boolean atualizou = conta.sacar(valor);
        if (atualizou == true) {
            return contaBancariaRepository.save(conta);
        } else {
            throw new RuntimeException("O valor enviado é inválido");
        }
    }

    public ContaBancaria ativarDesativarConta(Long id, boolean ativa) {
        return contaBancariaRepository.findById(id).map(conta -> {
            conta.setAtivo(ativa);
            return contaBancariaRepository.save(conta);
        }).orElseThrow(() -> new RuntimeException("Ocorreu um erro no sistema"));
    }
}
