import React, { useState } from 'react';

const CourseEnrollmentDashboard = () => {
  const [studentsMap, setStudentsMap] = useState(new Map());
  const [filterCourse, setFilterCourse] = useState('');

  const addStudent = (id, name, coursesArray, gpa) => {
    const newStudent = {
      id,
      name,
      enrolledCourses: new Set(coursesArray),
      gpa
    };

    setStudentsMap(new Map([...studentsMap, [id, newStudent]]));
  };

  const removeStudent = (id) => {
    const newMap = new Map(studentsMap);
    newMap.delete(id);
    setStudentsMap(newMap);
  };

  const studentsArray = Array.from(studentsMap.values());

  const allUniqueCourses = Array.from(
    studentsArray.reduce((acc, student) => {
      student.enrolledCourses.forEach(course => acc.add(course));
      return acc;
    }, new Set())
  );

  const displayedStudents = studentsArray
    .filter(student =>
      filterCourse === '' || student.enrolledCourses.has(filterCourse)
    )
    .sort((a, b) => b.gpa - a.gpa);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Course Enrollment Dashboard</h1>

      <div className="mb-4">
        <label className="mr-2">Filter by Course:</label>
        <select
          onChange={(e) => setFilterCourse(e.target.value)}
          value={filterCourse}
        >
          <option value="">All Courses</option>
          {allUniqueCourses.map(course => (
            <option key={course} value={course}>
              {course}
            </option>
          ))}
        </select>
      </div>

      <table className="min-w-full border">
        <thead>
          <tr className="bg-gray-100">
            <th>Name</th>
            <th>GPA</th>
            <th>Courses</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {displayedStudents.map(student => (
            <tr key={student.id} className="border-t">
              <td>{student.name}</td>
              <td>{student.gpa}</td>
              <td>{Array.from(student.enrolledCourses).join(', ')}</td>
              <td>
                <button
                  onClick={() => removeStudent(student.id)}
                  className="text-red-500"
                >
                  Remove
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CourseEnrollmentDashboard;
