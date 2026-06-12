import java.util.*;
import java.util.stream.*;

class Student {
    int id;
    String name;
    List<String> courses;
    Map<String, Integer> scores;

    public Student(int id, String name, List<String> courses, Map<String, Integer> scores) {
        this.id = id;
        this.name = name;
        this.courses = courses;
        this.scores = scores;
    }

    public double getAverageScore() {
        if(scores.isEmpty()) return 0;
        int total = scores.values().stream().mapToInt(Integer::intValue).sum();
        return (double) total / scores.size();
    }

    @Override
    public String toString() {
        return id + " " + name + " Avg:" + getAverageScore();
    }
}

public class StudentAnalyzer {

    public static List<Student> getTopNStudents(List<Student> students, int n) {
        return students.stream()
                .sorted(Comparator.comparingDouble(Student::getAverageScore).reversed())
                .limit(n)
                .collect(Collectors.toList());
    }

    public static Map<String, Double> getAverageScorePerCourse(List<Student> students) {
        Map<String, Integer> total = new HashMap<>();
        Map<String, Integer> count = new HashMap<>();

        for(Student s : students) {
            for(String course : s.courses) {
                int score = s.scores.getOrDefault(course, 0);
                total.put(course, total.getOrDefault(course, 0) + score);
                count.put(course, count.getOrDefault(course, 0) + 1);
            }
        }

        Map<String, Double> avg = new HashMap<>();
        for(String course : total.keySet()) {
            avg.put(course, (double) total.get(course) / count.get(course));
        }
        return avg;
    }

    public static Set<String> getAllUniqueCourses(List<Student> students) {
        return students.stream()
                .flatMap(s -> s.courses.stream())
                .collect(Collectors.toSet());
    }

    public static void main(String[] args) {
        List<Student> students = new ArrayList<>();

        Map<String,Integer> scores1 = new HashMap<>();
        scores1.put("DSA",90);
        scores1.put("Math",80);

        Map<String,Integer> scores2 = new HashMap<>();
        scores2.put("DSA",70);
        scores2.put("Math",85);
        scores2.put("OS",88);

        Map<String,Integer> scores3 = new HashMap<>();
        scores3.put("DSA",95);
        scores3.put("OS",91);

        students.add(new Student(1,"Rahul", Arrays.asList("DSA","Math"),scores1));
        students.add(new Student(2,"Anita", Arrays.asList("DSA","Math","OS"),scores2));
        students.add(new Student(3,"Ravi", Arrays.asList("DSA","OS"),scores3));

        System.out.println("Top 2 Students:");
        List<Student> top = getTopNStudents(students,2);
        top.forEach(System.out::println);

        System.out.println("\nAverage Score Per Course:");
        Map<String,Double> avg = getAverageScorePerCourse(students);
        avg.forEach((k,v) -> System.out.println(k + " : " + v));

        System.out.println("\nAll Unique Courses:");
        Set<String> courses = getAllUniqueCourses(students);
        System.out.println(courses);
    }
}