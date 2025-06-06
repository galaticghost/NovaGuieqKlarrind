package com.example.demotres.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demotres.model.Produto;

public interface ProdutoRepository extends JpaRepository<Produto,Long> {
    
}
