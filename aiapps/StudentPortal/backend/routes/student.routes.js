const express = require('express');
const { auth, isAdmin } = require('../middleware/auth.middleware');
const { User, Course, Enrollment, Assignment } = require('../models');
const router = express.Router();

// Get all students (admin only)
router.get('/', auth, isAdmin, async (req, res) => {
  try {
    const users = await User.findAll({
      where: { role: 'student' },
      attributes: { exclude: ['password'] }
    });
    res.send(users);
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch students' });
  }
});

// Get student profile
router.get('/:id', auth, async (req, res) => {
  try {
    const user = await User.findByPk(req.params.id, {
      attributes: { exclude: ['password'] }
    });
    if (!user) {
      return res.status(404).send({ error: 'Student not found' });
    }
    res.send(user);
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch student profile' });
  }
});

// Update student profile
router.put('/:id', auth, async (req, res) => {
  try {
    const updates = Object.keys(req.body);
    const allowedUpdates = ['name', 'email', 'contact'];
    const isValidOperation = updates.every(update => allowedUpdates.includes(update));

    if (!isValidOperation) {
      return res.status(400).send({ error: 'Invalid updates!' });
    }

    const user = await User.findByPk(req.params.id);
    if (!user) {
      return res.status(404).send({ error: 'Student not found' });
    }

    // Only allow users to update their own profile unless they're an admin
    if (req.user.id !== user.id && req.user.role !== 'admin') {
      return res.status(403).send({ error: 'Not authorized to update this profile' });
    }

    updates.forEach(update => user[update] = req.body[update]);
    await user.save();
    
    // Don't send password in response
    const userResponse = user.toJSON();
    delete userResponse.password;
    
    res.send(userResponse);
  } catch (error) {
    res.status(400).send({ error: 'Failed to update profile' });
  }
});

// Get student enrollments
router.get('/:id/enrollments', auth, async (req, res) => {
  try {
    // Verify the student exists
    const user = await User.findByPk(req.params.id);
    if (!user) {
      return res.status(404).send({ error: 'Student not found' });
    }

    // Only allow users to view their own enrollments unless they're an admin
    if (req.user.id !== user.id && req.user.role !== 'admin') {
      return res.status(403).send({ error: 'Not authorized to view these enrollments' });
    }

    const enrollments = await Course.findAll({
      include: [{
        model: User,
        where: { id: req.params.id },
        through: { attributes: [] }, // Don't include join table fields
        attributes: [] // Don't include user fields
      }]
    });

    res.send(enrollments);
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch enrollments' });
  }
});

// Get student assignments
router.get('/:id/assignments', auth, async (req, res) => {
  try {
    // Verify the student exists
    const user = await User.findByPk(req.params.id);
    if (!user) {
      return res.status(404).send({ error: 'Student not found' });
    }

    // Only allow users to view their own assignments unless they're an admin
    if (req.user.id !== user.id && req.user.role !== 'admin') {
      return res.status(403).send({ error: 'Not authorized to view these assignments' });
    }

    const enrollments = await Enrollment.findAll({
      where: { studentId: req.params.id },
      include: [{
        model: Course,
        include: [{
          model: Assignment,
          attributes: ['id', 'title', 'description', 'dueDate']
        }]
      }]
    });

    // Flatten the assignments array and add course information
    const assignments = enrollments.flatMap(enrollment => 
      enrollment.Course.Assignments.map(assignment => ({
        ...assignment.toJSON(),
        courseName: enrollment.Course.title,
        courseId: enrollment.Course.id
      }))
    );

    res.send(assignments);
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch assignments' });
  }
});

module.exports = router; 