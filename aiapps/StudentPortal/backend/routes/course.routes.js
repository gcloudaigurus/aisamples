const express = require('express');
const { auth, isAdmin } = require('../middleware/auth.middleware');
const { Course, Assignment } = require('../models');
const router = express.Router();

// Get all courses
router.get('/', auth, async (req, res) => {
  try {
    const courses = await Course.findAll();
    res.send(courses);
  } catch (error) {
    res.status(500).send(error);
  }
});

// Create a course (admin only)
router.post('/', auth, isAdmin, async (req, res) => {
  try {
    const course = await Course.create(req.body);
    res.status(201).send(course);
  } catch (error) {
    res.status(400).send(error);
  }
});

// Get course by ID
router.get('/:id', auth, async (req, res) => {
  try {
    const course = await Course.findByPk(req.params.id, {
      include: [Assignment]
    });
    
    if (!course) {
      return res.status(404).send({ error: 'Course not found' });
    }
    
    res.send(course);
  } catch (error) {
    res.status(500).send(error);
  }
});

// Update course (admin only)
router.put('/:id', auth, isAdmin, async (req, res) => {
  try {
    const course = await Course.findByPk(req.params.id);
    if (!course) {
      return res.status(404).send({ error: 'Course not found' });
    }

    const updates = Object.keys(req.body);
    updates.forEach(update => course[update] = req.body[update]);
    await course.save();
    
    res.send(course);
  } catch (error) {
    res.status(400).send(error);
  }
});

// Delete course (admin only)
router.delete('/:id', auth, isAdmin, async (req, res) => {
  try {
    const course = await Course.findByPk(req.params.id);
    if (!course) {
      return res.status(404).send({ error: 'Course not found' });
    }

    await course.destroy();
    res.send({ message: 'Course deleted successfully' });
  } catch (error) {
    res.status(500).send(error);
  }
});

// Get course assignments
router.get('/:id/assignments', auth, async (req, res) => {
  try {
    const assignments = await Assignment.findAll({
      where: { courseId: req.params.id }
    });
    res.send(assignments);
  } catch (error) {
    res.status(500).send(error);
  }
});

module.exports = router; 