import java.util.*;
import java.lang.*;
import java.io.*;


public class creaDatos{
    public static void main(String args[]){
        /////Inicialización/////
        double Vo = 90;
        double So = 2036;
        double tMuestra = 0.1;
        /////Entrada/////
        double porFrenada[] =  {0,0,0,0,0,0,0,0,0,0,/*10*/
                                0,0,0,0,0,0,0,0,0,0,/*20*/
                                0,0,0,0,0,0,0,0,0,0,/*30*/
                                0,0,0,0,0,0,0,0,0,0,/*40*/
                                0,0,0,0,0,0,0,0,0,0,/*50*/
                                0,0,0,0,0,0,0,0,0,0,/*60*/
                                0,0,0,0,0,0,0,0,0,0,/*70*/
                                0,0,0,0,0,0,0,0,0,0,/*80*/
                                0,0,0,0,0,0,0,0,0,0,/*90*/
                                0,0,0,0,0,0,0,0,0,0,/*100*/
                                0.02,0.28,0.739,0.97,1,1,1,1,1,1,/*110*/
                                1,1,1,1,1,1,1,1,1,1,/*120*/
                                1,1,1,1,1,0.89,0.9,0.674,0.735,0.632,/*130*/
                                0.329,0.144,0,0,0,0,0,0.62,0.741,0.762,/*140*/
                                0.41,0.172,0.207,0,0,0,0,0,0.26,0.34,/*150*/
                                0.307,0.284,0.274,0.295,0.39,0.28,0.04,0,0,0,/*160*/
                                0,0,0,0,0,0,0,0,0,0,/*170*/
                                0,0,0,0,0,0,0,0,0,0,/*180*/
                                0,0,0,0,0,0,0,0,0,0,/*190*/
                                0,0,0,0,0,0,0,0,0,0,/*200*/
                                0,0,0,0,0,0,0,0,0,0,/*210*/
                                0,0,0,0,0,0,0,0,0,0,/*220*/
                                0,0,0,0,0,0,0,0,0,0,/*230*/
                                0.13,0.24,0.48,0.89,1,1,1,1,1,1,/*240*/
                                0.93,0.74,0.58,0.39,0.17,0.074,0.06,0,0,0,/*250*/
                                0,0,0,0,0,0,0,0,0,0,/*260*/
                                0,0,0,0,0,0,0,0,0,0,/*270*/
                                0,0,0,0,0,0,0,0,0,0,/*280*/
                                0,0,0,0,0,0,0,0,0,0,/*290*/
                                0,0,0,0,0,0,0,0,0,0/*300*/};

        double porAceleracion[] =  {1,1,1,1,1,1,1,1,1,1,/*10*/
                                    1,1,1,1,1,1,1,1,1,1,/*20*/
                                    1,1,1,1,1,1,1,1,1,1,/*30*/
                                    1,1,1,1,1,1,1,1,1,1,/*40*/
                                    1,1,1,1,1,1,1,1,1,1,/*50*/
                                    1,1,1,1,1,1,1,1,1,1,/*60*/
                                    1,1,1,1,1,1,1,1,1,1,/*70*/
                                    1,1,1,1,1,1,1,1,1,1,/*80*/
                                    1,1,1,1,1,1,1,1,1,1,/*90*/
                                    1,1,1,1,1,1,1,1,1,1,/*100*/
                                    0.398,0.09,0,0,0,0,0,0,0,0,/*110*/
                                    0,0,0,0,0,0,0,0,0,0,/*120*/
                                    0,0,0,0,0,0,0,0,0,0.127,/*130*/
                                    0.227,0.478,0.94,1,1,1,1,0.24,0,0,/*140*/
                                    0,0,0.45,0.68,0.53,0.38,0.417,0.254,0.195,0.127,/*150*/
                                    0.098,0.09,0.38,0.21,0.34,0.67,0.98,1,1,1,/*160*/
                                    1,1,1,1,1,1,1,1,1,1,/*170*/
                                    1,1,1,1,1,1,1,1,1,1,/*180*/
                                    1,1,1,1,1,1,1,1,1,1,/*190*/
                                    1,1,1,1,1,1,1,1,1,1,/*200*/
                                    1,1,1,1,1,1,1,1,1,1,/*210*/
                                    1,1,1,1,1,1,1,1,1,1,/*220*/
                                    1,1,1,1,1,1,1,1,1,1,/*230*/
                                    0.73,0.21,0,0,0,0,0,0,0,0,/*240*/
                                    0,0,0,0.37,0.84,1,1,1,1,1,/*250*/
                                    1,1,1,1,1,1,1,1,1,1,/*260*/
                                    1,1,1,1,1,1,1,1,1,1,/*270*/
                                    1,1,1,1,1,1,1,1,1,1,/*280*/
                                    1,1,1,1,1,1,1,1,1,1,/*290*/
                                    1,1,1,1,1,1,1,1,1,1/*300*/};
        /////Salida/////
        double rpm[] = new double[(porAceleracion.length)];
        double marcha[] = new double[(porAceleracion.length)];
        double velocidad[] = new double[(porAceleracion.length)];
        double metros[] = new double[(porAceleracion.length)];

        /////Proceso de creación de datos/////
        for(int i =0; i < (porAceleracion.length); i++){
            /////inicialización de tamaño/////
            // rpm = new double[(porAceleracion.length)];
            // velocidad = new double[(porAceleracion.length)];
            // metros = new double[(porAceleracion.length)];
            // marcha = new double[(porAceleracion.length)];

            /////variables auxiliares/////
            double V;
            double porA;
            double porF;
            double increA;
            double increF; 

            /////llamada de los métodos/////
            porA = porAceleracion[i];
            increA = acelera(Vo, porA, tMuestra);

            porF = porFrenada[i];
            increF = frenada(Vo, porF, tMuestra);

            velocidad[i] = Vo + increA + increF;

            marcha[i] = transmision(velocidad[i], i);
            rpm[i] = revolucion(velocidad[i], i);

            metros[i] = GPS(Vo, velocidad[i], So, tMuestra);

            Vo = velocidad[i];
            So = metros[i];

        }
        
        /////Escritura en archivo.csv/////
        PrintWriter pw;
        try{
            pw = new PrintWriter(new File("datos.csv"));

            StringBuffer csvHeader = new StringBuffer("");
            StringBuffer csvData = new StringBuffer("");
            csvHeader.append("Distancia,velocidad,%frenado,revoluciones,marcha\n");

            // write header
            pw.write(csvHeader.toString());

            // write data
            for(int i = 0; (i < porAceleracion.length); i++){
                csvData.append(Double.toString(metros[i]));
                csvData.append(',');
                csvData.append(Double.toString(velocidad[i]));
                csvData.append(',');
                csvData.append(Double.toString(porFrenada[i]));
                csvData.append(',');
                csvData.append(Double.toString(rpm[i]));
                csvData.append(',');
                csvData.append(Double.toString(marcha[i]));
                csvData.append('\n');
                
            }
            pw.write(csvData.toString());
            pw.close();
            
        }catch(Exception e){
            System.out.println("Se ha producido el error: " + e);
        }




    }
/////Métodos que modelizan cosas/////

    public static double acelera(double Vant, double porA, double tMuestra){
        double divi = (208*208)/(Vant*Vant);
        double numero = 360.058258278995/(divi - 1);
        double inst = Math.sqrt(numero);
        inst += tMuestra;

        double V = 208*(inst/(Math.sqrt((inst*inst) + 360.058258278995)));

        double incre = (porA/1)*(V-Vant);

        return incre;
    }
    
    public static double frenada(double Vant, double porF, double tMuestra){
        double multi = 26.82458782989084 * 4.8463;
        double inst = (Vant - 130 + multi) / 26.82458782989084;
        inst -= tMuestra;

        double VF = 130 + 26.82458782989084*(inst - 4.8463);
        double incre = (porF/1)*(VF - Vant);

        return incre;
    }

    public static double transmision (double V, int j){
        double trans = 0;
        if(V <= 50.4){
            trans = 1;
        }else if((V > 50.4) && (V <= 80.03)) {
            trans = 2;
        }else if((V > 80.03) && (V <= 113.8)){
            trans = 3;
        }else if((V > 113.8) && (V <= 153.6)){
            trans = 4;
        }else if((V > 153.6) && (V <= 242)){
            trans = 5;
        }
        return trans;
    }

    public static double revolucion(double V, int j){
        double revol = 0;
        if(V <= 50.4){
            revol = 7000 + (111.11)*(V - 63);
        }else if((V > 50.4) && (V <= 80.03)) {
            revol = 7000 + (70)*(V - 100);
        }else if((V > 80.03) && (V <= 113.8)){
            revol = 7000 + (47.9452)*(V - 143);
        }else if((V > 113.8) && (V <= 153.6)){
            revol = 7000 + (36.458)*(V - 192);
        }else if((V > 153.6) && (V <= 242)){
            revol = 7000 + (28.9256)*(V - 242);
        }
        return revol;
    }

    public static double GPS (double Vant, double V,double Sant, double tMuestra){
        V = V*0.277777778;
        Vant = Vant*0.277777778;
        double incre = (V - Vant);
        double s = Sant + Vant*tMuestra + incre/2;
        return s;
    }
}

// String archCSV = "datos.csv";
            // CSVWriter csvWriter = new csvWriter(new FileWriter(archCSV));

            // List<double[]> trama = new ArrayList<double[]>();
            // for(int i = 0; (i < porAceleracion.length); i++){
            //     double[] aux = {metros[i], rpm[i], velocidad[i], marcha[i], porFrenada[i]};
            //     trama.add(aux);
            // }

            // writer.writeAll(trama);
