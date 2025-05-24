package com.example.demodois.repository;

import com.example.demodois.model.Cliente;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ClienteRepository extends JpaRepository<Cliente,Long>  {
    
}
