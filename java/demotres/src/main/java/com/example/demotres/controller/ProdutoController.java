package com.example.demotres.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.example.demotres.repository.ProdutoRepository;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;

import com.example.demotres.model.Produto;
import java.util.List;
import org.springframework.web.bind.annotation.RequestBody;;

@RestController
@RequestMapping("/produtos")
public class ProdutoController {
    private final ProdutoRepository repository;
    
    public ProdutoController(ProdutoRepository repository){
        this.repository = repository;
    }

    @GetMapping
    public List<Produto> listar (){
        return repository.findAll();
    }

    @PostMapping
    public Produto inserir(@RequestBody Produto entity){
        return repository.save(entity);
    }

    @PutMapping("/{id}")
    public Produto atualizar(@PathVariable Long id, @RequestBody Produto produto) {
        produto.setId(id);
        return repository.save(produto);
    }


    @DeleteMapping("/{id}")
    public void remover(@PathVariable Long id) {
        repository.deleteById(id);
    }

}

