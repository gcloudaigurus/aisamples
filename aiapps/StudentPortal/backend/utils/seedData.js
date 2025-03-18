const { Course, User, Assignment } = require('../models');
const bcrypt = require('bcryptjs');

const sampleCourses = [
  {
    title: 'Introduction to Computer Science',
    description: 'Learn the fundamentals of computer science, including algorithms, data structures, and programming concepts.',
    instructor: 'Dr. Alan Turing'
  },
  {
    title: 'Web Development Fundamentals',
    description: 'Master HTML, CSS, and JavaScript to build modern responsive websites. Learn about frontend frameworks and backend integration.',
    instructor: 'Sarah Johnson'
  },
  {
    title: 'Data Science and Analytics',
    description: 'Explore data analysis, visualization, and machine learning techniques using Python and popular data science libraries.',
    instructor: 'Dr. Maria Chen'
  },
  {
    title: 'Mobile App Development',
    description: 'Build native mobile applications for iOS and Android using React Native and modern mobile development practices.',
    instructor: 'James Smith'
  },
  {
    title: 'Artificial Intelligence Basics',
    description: 'Introduction to AI concepts, machine learning algorithms, and practical applications in modern technology.',
    instructor: 'Dr. Robert Brown'
  },
  {
    title: 'Database Management Systems',
    description: 'Learn about database design, SQL, NoSQL, and modern database management practices.',
    instructor: 'Emily Davis'
  }
];

const sampleAssignments = [
  {
    courseId: 1,
    title: 'Algorithm Implementation',
    description: 'Implement basic sorting and searching algorithms in your preferred programming language.',
    dueDate: new Date(Date.now() + 14 * 24 * 60 * 60 * 1000) // 14 days from now
  },
  {
    courseId: 1,
    title: 'Data Structures Project',
    description: 'Create a program that demonstrates the use of different data structures.',
    dueDate: new Date(Date.now() + 21 * 24 * 60 * 60 * 1000) // 21 days from now
  },
  {
    courseId: 2,
    title: 'Personal Portfolio Website',
    description: 'Build a responsive portfolio website using HTML, CSS, and JavaScript.',
    dueDate: new Date(Date.now() + 10 * 24 * 60 * 60 * 1000) // 10 days from now
  },
  {
    courseId: 2,
    title: 'JavaScript Application',
    description: 'Create a single-page application using modern JavaScript frameworks.',
    dueDate: new Date(Date.now() + 20 * 24 * 60 * 60 * 1000) // 20 days from now
  },
  {
    courseId: 3,
    title: 'Data Analysis Report',
    description: 'Analyze a provided dataset and create a comprehensive report with visualizations.',
    dueDate: new Date(Date.now() + 15 * 24 * 60 * 60 * 1000) // 15 days from now
  },
  {
    courseId: 4,
    title: 'Mobile App Prototype',
    description: 'Design and implement a basic mobile application with React Native.',
    dueDate: new Date(Date.now() + 25 * 24 * 60 * 60 * 1000) // 25 days from now
  }
];

const sampleAdmin = {
  name: 'Admin User',
  email: 'admin@example.com',
  password: 'admin123',
  role: 'admin',
  contact: '123-456-7890'
};

const seedDatabase = async () => {
  try {
    // Create admin user if it doesn't exist
    const existingAdmin = await User.findOne({ where: { email: sampleAdmin.email } });
    if (!existingAdmin) {
      await User.create(sampleAdmin);
      console.log('Admin user created successfully');
    }

    // Create sample courses
    const existingCourses = await Course.findAll();
    if (existingCourses.length === 0) {
      const courses = await Course.bulkCreate(sampleCourses);
      console.log('Sample courses created successfully');

      // Create sample assignments
      const assignments = sampleAssignments.map(assignment => ({
        ...assignment,
        courseId: courses[assignment.courseId - 1].id // Map to actual course IDs
      }));
      await Assignment.bulkCreate(assignments);
      console.log('Sample assignments created successfully');
    }

  } catch (error) {
    console.error('Error seeding database:', error);
  }
};

module.exports = seedDatabase; 