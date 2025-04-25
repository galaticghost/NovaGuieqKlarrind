import java.util.ArrayList;

public class SistemaHospital {
    private ArrayList<Paciente> pacientes = new ArrayList<>();
    private ArrayList<Consulta> consultas = new ArrayList<>();

    public void cadastrarPaciente(String nome, String cpf, int idade, String telefone) {
        pacientes.add(new Paciente(nome, cpf, idade, telefone));
        System.out.println("Paciente cadastrado com sucesso!");
    }

    public void agendarConsulta(String cpf, String data, String horario, String especialidade, String medico) {
        Paciente pacienteEncontrado = null;
        for (Paciente p : pacientes) {
            if (p.getCpf().equals(cpf)) {
                pacienteEncontrado = p;
                break;
            }
        }
        if (pacienteEncontrado != null) {
            consultas.add(new Consulta(pacienteEncontrado, data, horario, especialidade, medico));
            System.out.println("Consulta agendada com sucesso!");
        } else {
            System.out.println("Paciente não encontrado!");
        }
    }

    public void listarConsultasPaciente(String cpf) {
        boolean encontrou = false;
        for (Consulta c : consultas) {
            if (c.getCpfPaciente().equals(cpf)) {
                c.exibirDetalhes();
                encontrou = true;
            }
        }
        if (!encontrou) {
            System.out.println("Nenhuma consulta encontrada para este CPF.");
        }
    }

    public void listarPacientes() {
        if (pacientes.isEmpty()) {
            System.out.println("Não há nenhum paciente cadastrado no sistema");
        }
        for (Paciente paciente : pacientes) {
            paciente.exibirInformacoes();
        }
    }

    public void listarConsultasData(String data) {
        Boolean consultas_existem = false;
        for (Consulta consulta : consultas) {
            if (consulta.getData().equals(data)) {
                consulta.exibirDetalhes();
                consultas_existem = true;
            }
        }
        if (!consultas_existem) {
            System.out.println("Não há consultas nessa data");
        }
    }
}