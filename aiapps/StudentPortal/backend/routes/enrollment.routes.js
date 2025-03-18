const express = require('express');
const { auth } = require('../middleware/auth.middleware');
const { Enrollment, Course } = require('../models');
const router = express.Router();

// Get all enrollments for the current user
router.get('/', auth, async (req, res) => {
  try {
    const enrollments = await Enrollment.findAll({
      where: { studentId: req.user.id },
      include: [Course]
    });
    res.send(enrollments);
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch enrollments' });
  }
});

// Enroll in a course
router.post('/', auth, async (req, res) => {
  try {
    // Check if the course exists
    const course = await Course.findByPk(req.body.courseId);
    if (!course) {
      return res.status(404).send({ error: 'Course not found' });
    }

    // Check if already enrolled
    const existingEnrollment = await Enrollment.findOne({
      where: {
        studentId: req.user.id,
        courseId: req.body.courseId
      }
    });

    if (existingEnrollment) {
      return res.status(400).send({ error: 'Already enrolled in this course' });
    }

    const enrollment = await Enrollment.create({
      studentId: req.user.id,
      courseId: req.body.courseId
    });

    // Include course details in response
    const enrollmentWithCourse = await Enrollment.findByPk(enrollment.id, {
      include: [Course]
    });

    res.status(201).send(enrollmentWithCourse);
  } catch (error) {
    res.status(400).send({ error: 'Failed to enroll in course' });
  }
});

// Unenroll from a course
router.delete('/:courseId', auth, async (req, res) => {
  try {
    const enrollment = await Enrollment.findOne({
      where: {
        courseId: req.params.courseId,
        studentId: req.user.id
      }
    });

    if (!enrollment) {
      return res.status(404).send({ error: 'Enrollment not found' });
    }

    await enrollment.destroy();
    res.send({ message: 'Successfully unenrolled from course' });
  } catch (error) {
    res.status(500).send({ error: 'Failed to unenroll from course' });
  }
});

module.exports = router; 