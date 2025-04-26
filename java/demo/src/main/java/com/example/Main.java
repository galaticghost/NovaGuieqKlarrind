package com.example;

import com.google.gson.*;
import com.google.gson.reflect.TypeToken;

import java.io.FileReader;
import java.lang.reflect.Type;
import java.util.List;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        try {
            Gson gson = new GsonBuilder().setPrettyPrinting().create();
            FileReader reader = new FileReader("produtos.json");

            Type listType = new TypeToken<List<Map<String, Object>>>(){}.getType();
            List<Map<String, Object>> produtos = gson.fromJson(reader, listType);

            int count = 1;
            for (Map<String, Object> produto : produtos) {
                System.out.println("╔═══════════════════════════════════════════════╗");
                System.out.printf("║ Produto %d\n", count++);
                System.out.println("╠═══════════════════════════════════════════════╣");

                for (Map.Entry<String, Object> entry : produto.entrySet()) {
                    String chave = entry.getKey();
                    Object valor = entry.getValue();

                    // Tratar arrays
                    if (valor instanceof List<?>) {
                        List<?> lista = (List<?>) valor;
                        System.out.printf("║ %-20s: %s\n", chave, lista.toString());
                    }
                    // Tratar objetos internos
                    else if (valor instanceof Map<?, ?>) {
                        Map<?, ?> mapa = (Map<?, ?>) valor;
                        System.out.printf("║ %-20s:\n", chave);
                        for (Map.Entry<?, ?> e : mapa.entrySet()) {
                            System.out.printf("║    -> %-16s: %s\n", e.getKey(), e.getValue());
                        }
                    }
                    // Valor simples
                    else {
                        System.out.printf("║ %-20s: %s\n", chave, valor);
                    }
                }

                System.out.println("╚═══════════════════════════════════════════════╝\n");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

