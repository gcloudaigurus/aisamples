const sequelize = require('../config/database');
const User = require('./user.model');
const Course = require('./course.model');
const Enrollment = require('./enrollment.model');
const Assignment = require('./assignment.model');
const Attendance = require('./attendance.model');

// Define associations
User.belongsToMany(Course, { through: Enrollment, foreignKey: 'studentId' });
Course.belongsToMany(User, { through: Enrollment, foreignKey: 'courseId' });

Course.hasMany(Assignment, { foreignKey: 'courseId' });
Assignment.belongsTo(Course, { foreignKey: 'courseId' });

User.hasMany(Attendance, { foreignKey: 'studentId' });
Attendance.belongsTo(User, { foreignKey: 'studentId' });
Course.hasMany(Attendance, { foreignKey: 'courseId' });
Attendance.belongsTo(Course, { foreignKey: 'courseId' });

module.exports = {
  sequelize,
  User,
  Course,
  Enrollment,
  Assignment,
  Attendance
}; 