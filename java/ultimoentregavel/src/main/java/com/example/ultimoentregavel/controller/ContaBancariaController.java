package com.example.ultimoentregavel.controller;

import java.util.List;
import java.util.Map;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.ultimoentregavel.model.ContaBancaria;
import com.example.ultimoentregavel.service.ContaBancariaService;

@RestController
@RequestMapping("/contas")
public class ContaBancariaController {
    private final ContaBancariaService contaBancariaService;

    public ContaBancariaController(ContaBancariaService contaBancariaService) {
        this.contaBancariaService = contaBancariaService;
    }

    @PostMapping
    public ContaBancaria criarConta(@RequestBody ContaBancaria contaBancaria) {
        return contaBancariaService.criarConta(contaBancaria);
    }

    @GetMapping
    public List<ContaBancaria> buscarTodasContas() {
        return contaBancariaService.buscarTodasContas();
    }

    @GetMapping("/{id}")
    public ContaBancaria buscarContaPorId(@PathVariable Long id) {
        return contaBancariaService.buscarContaPorId(id);
    }

    @PutMapping("/{id}/depositar")
    public ContaBancaria depositar(@PathVariable Long id, @RequestBody Map<String, Double> payload) {
        return contaBancariaService.depositar(id, payload.get("valor"));
    }

    @PutMapping("/{id}/sacar")
    public ContaBancaria sacar(@PathVariable Long id, @RequestBody Map<String, Double> payload) {
        return contaBancariaService.sacar(id, payload.get("valor"));
    }

    @PutMapping("/{id}/status")
    public ContaBancaria ativarDesativarConta(@PathVariable Long id, @RequestParam boolean ativa) {
        return contaBancariaService.ativarDesativarConta(id, ativa);
    }
}