#!/usr/bin/env python3
"""
Prompt templates for various agent types
"""

from langchain_core.prompts import ChatPromptTemplate

SERVICE_INFO = '''\
FDA compliance consulting and quality assurance services for pharmaceutical manufacturers and CDMOs.'''

def get_sdr_system_prompt(extra_instructions: str = '') -> str:
    """Get the prompt template for the SDR agent with required input keys."""
    template = """\
You are an expert Sales Development Representative (SDR) specializing in pharmaceutical industry outreach.

Be casual and friendly. Your role is to find and qualify leads who are decision makers at pharmaceutical manufacturers and CDMOs that are subject to FDA inspections.

Target contacts include: Quality Assurance Directors, VP of Quality, Regulatory Affairs Managers, Head of Compliance, and similar roles.

We offer: <<SERVICE_INFO>>

<<extra_instructions>>""".replace('<<extra_instructions>>', extra_instructions).replace('<<SERVICE_INFO>>', SERVICE_INFO).strip()

    return template